from datetime import datetime
from django import forms
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
# from django.db.models import Avg, Count, Max, Min, Sum
# Post.objects.aggregate(Max("id"))

from .models import Item, Archive, Comment
from .forms import ItemCreateForm, ItemSellForm, CommentForm


@login_required
def index(request):
    items = Item.objects.filter(buyer=request.user).filter()
    # for item in items:
    #     print(item.purchase_unit_price)
    form = CommentForm()
    comments = Comment.objects.all()
    context = {
        'items': items,
        'form': form,
        'comments': comments,
    }
    return render(request, 'index.html', context)


@login_required
def archive(request):
    sold_items = Archive.objects.filter(seller=request.user)
    print(sold_items)
    context = {
        'sold_items': sold_items,
    }
    return render(request, 'archive.html', context)


@login_required
def item_create(request):
    form = ItemCreateForm(
        request.POST or None,
        files=request.FILES or None,
    )
    if form.is_valid():
        item = form.save(commit=False)
        item.buyer = request.user
        item.save()
        return redirect('items:index')
    return render(request, 'items/edit_item.html', {'form': form})


@login_required
def item_edit(request, item_id):
    item = get_object_or_404(Item, id=item_id)
    if item.buyer != request.user:
        return redirect('items:index')
    form = ItemCreateForm(
        request.POST or None,
        files=request.FILES or None,
        instance=item
    )
    form.fields['purchase_unit_price'].widget.attrs['readonly'] = True
    # form.fields['purchase_unit_price'].widget.attrs['disabled'] = True
    # При такой настройке форма не сохраняется
    # form.fields['count'].widget = forms.HiddenInput()
    # Поле становится невидимым, но виды verbose и help texts
    if form.is_valid():
        form.save()
        return redirect('items:index')
    context = {
        'form': form,
        'is_edit': True,
        'item_id': item_id,
    }
    return render(request, 'items/edit_item.html', context)


@login_required
def item_delete(request, item_id):
    item = get_object_or_404(Item, id=item_id)
    if item.buyer != request.user:
        return redirect('items:index')
    item.delete()
    return redirect('items:index')


@login_required
def item_sell(request, item_id):
    item = get_object_or_404(Item, id=item_id)
    if item.buyer != request.user:
        return redirect('items:index')
    form_count = item.count
    form = ItemSellForm(
        form_count,
        request.POST or None,
        initial={'sell_date': lambda: datetime.now(),
                 'sell_price': None}
    )

    if form.is_valid():
        sold_item = form.save(commit=False)
        sold_item.seller = request.user
        sold_item.item = item
        sold_item.save()
        sold_count = int(form.cleaned_data['count'])
        item.count -= sold_count
        item.sold_count += sold_count
        item.earnings += form.cleaned_data['sell_unit_price'] * sold_count
        item.save()

        return redirect('items:index')
    context = {
        'form': form,
        'is_sell': True,
    }
    return render(request, 'items/edit_item.html', context)


@login_required
def item_revoke(request, item_id):
    sold_item = get_object_or_404(Archive, id=item_id)
    item = get_object_or_404(Item, id=sold_item.item_id)
    if sold_item.seller != request.user:
        return redirect('items:archive')
    item.count += sold_item.count
    item.sold_count -= sold_item.count
    item.earnings -= sold_item.sell_unit_price * sold_item.count
    item.save()
    sold_item.delete()
    return redirect('items:archive')


@login_required
def item_comment(request, item_id):
    sold_item = get_object_or_404(Archive, id=item_id)
    if sold_item.seller != request.user:
        return redirect('items:archive')
    form_count = False
    form = ItemSellForm(
        form_count,
        request.POST or None,
        instance=sold_item
    )
    if form.is_valid():
        form.save()
        return redirect('items:archive')
    context = {
        'form': form,
        'is_edit': True,
        'item_id': item_id,
    }
    return render(request, 'items/edit_item.html', context)


@login_required
def add_comment(request):
    form = CommentForm(request.POST or None)
    if form.is_valid():
        comment = form.save(commit=False)
        comment.author = request.user
        comment.save()
    return redirect('items:index')

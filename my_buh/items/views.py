from datetime import datetime
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
# from django.db.models import Avg, Count, Max, Min, Sum
# Post.objects.aggregate(Max("id"))

from .models import Item, Archive
from .forms import ItemCreateForm, ItemSellForm


@login_required
def index(request):
    items = Item.objects.filter(owner=request.user)
    # for item in items:
    #     print(item.purchase_unit_price)
    context = {
        'items': items,
    }
    return render(request, 'index.html', context)


@login_required
def archive(request):
    sold_items = Archive.objects.filter(seller=request.user)
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
        item.owner = request.user
        item.save()
        return redirect('items:index')
    return render(request, 'items/edit_item.html', {'form': form})


@login_required
def item_edit(request, item_id):
    item = get_object_or_404(Item, id=item_id)
    if item.owner != request.user:
        return redirect('items:index')
    form = ItemCreateForm(
        request.POST or None,
        files=request.FILES or None,
        instance=item
    )
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
    if item.owner != request.user:
        return redirect('items:index')
    item.delete()
    return redirect('items:index')


@login_required
def item_sell(request, item_id):
    # item = get_object_or_404(Item, id=item_id)
    form = ItemSellForm(
        request.POST or None,
        initial={'sell_date': lambda: datetime.now(),
                 'sell_price': None}
    )
    if form.is_valid():
        sold_item = form.save(commit=False)
        sold_item.seller, sold_item.item_id = request.user, item_id
        sold_item.save()
        return redirect('items:index')
    context = {
        'form': form,
        'is_sell': True,
    }
    return render(request, 'items/edit_item.html', context)

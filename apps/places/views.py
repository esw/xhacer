from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponseRedirect, Http404
from django.template.context import RequestContext
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import permission_required,login_required
from django.views.generic import list_detail
from geo.models import City
from places.models import Place, Category, get_query
from places.forms import PlaceForm, PlaceCityForm

def place_detail(request,city_slug,place_slug):
    places_list = Place.objects.filter(city__slug=city_slug)

    return list_detail.object_detail(
        request,
        queryset = places_list,
        slug = place_slug,
        extra_context = {"city_slug" : city_slug}
    )

def city_list(request,city_slug=None, slug=None):
    try:
        city = City.objects.get(slug=city_slug)
    except City.DoesNotExist:
        raise Http404

    if slug :
        try:
            category = Category.objects.get(slug=slug)
            places_list = Place.objects.filter(city=city).filter(category=category)
        except Category.DoesNotExist:
            places_list = Place.objects.filter(city__slug=city_slug)

            return list_detail.object_detail(
                request,
                queryset = places_list,
                slug = slug,
                extra_context = {"city_slug" : city_slug}
            )
    else:
        places_list = Place.objects.filter(city=city)
        category = None

    categories = Category.objects.all()

    return list_detail.object_list(
        request,
        queryset = places_list,
        template_name = "places/city_places.html",
        template_object_name = "places",
        extra_context = {"city" : city, "category" : category, "categories" : categories}
    )

def place_search(request,city_slug=None):
    try:
        city = City.objects.get(name__iexact=city_slug)
    except City.DoesNotExist:
        raise Http404

    categories = Category.objects.all()

    query_string = ''
    places_list = None
    if ('q' in request.GET) and request.GET['q'].strip():
        query_string = request.GET['q']
        entry_query = get_query(query_string, ['name', 'desc',])
        places_list = Place.objects.filter(entry_query).order_by('name')

    return render_to_response('places/search_results.html',
                          { 'query_string': query_string,
                            'places_list': places_list,
                            'city' : city,
                            'categories' : categories },
                          context_instance=RequestContext(request))


@permission_required('places.add_place')
def place_city_add(request, city_slug):
    if request.method == 'POST':
        form = PlaceCityForm(request.POST)
        if form.is_valid():
            place = form.save(commit=False)
            place.city = get_object_or_404(City,slug=city_slug)
            place.save()
            return HttpResponseRedirect(place.get_absolute_url())
    else:
        form = PlaceCityForm()
        city = City.objects.get(name__iexact=city_slug)
        ''' nuevo '''
        if ('x' in request.GET) and ('y' in request.GET):
          x = request.GET['x']
          y = request.GET['y']
          return render_to_response('places/city_place_form.html', {
              'form':form, 'city':city, 'x' : x, 'y' : y,
          }, context_instance = RequestContext(request))

    return render_to_response('places/city_place_form.html', {
        'form':form, 'city':city,
    }, context_instance = RequestContext(request))

@permission_required('places.change_place')
def place_edit(request, city_slug, place_slug):
    place = get_object_or_404(Place,slug=place_slug,city__slug=city_slug)
    if request.method == 'POST':
        form = PlaceCityForm(request.POST, instance=place)
        if form.is_valid():
            place = form.save(commit=False)
            place.city = get_object_or_404(City,slug=city_slug)
            place.save()
            return HttpResponseRedirect(place.get_absolute_url())
    else:
        form = PlaceCityForm(instance=place)
    return render_to_response('places/city_place_form.html', {
        'form':form, 'place':place, 
    }, context_instance = RequestContext(request))



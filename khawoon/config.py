from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger


def pagination(request,data,num=10):
    paginator = Paginator(data, num)
    page = request.GET.get('page')

    try:
        iteams = paginator.page(page)
    except PageNotAnInteger:
        iteams = paginator.page(1)
    except EmptyPage:
        iteams = paginator.page(paginator.num_pages)

    index=iteams.number-1
    max_index=len(paginator.page_range)
    start_index=index-5 if index >=5 else 0
    end_index=index+5 if index<=max_index-5 else max_index
    page_range=paginator.page_range[start_index:end_index]
    return iteams,page_range
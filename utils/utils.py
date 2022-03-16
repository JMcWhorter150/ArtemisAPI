from math import ceil

async def paginate(filter, options, collection):
    sort_by = ''
    if (options.sortBy):
        sortingCriteria = []
        for sortOption in options.sortBy.split(','):
            key, order = sortOption.split(':')
            sortingCriteria.append(('-' if order == 'desc' else '') + key)
        sort_by = ' '.join(sortingCriteria)
    else:
        sort_by = 'createdAt'

    limit = options.get(limit) and int(options.limit, 10) if int(options.limit, 10) > 0 else 10
    page = options.get(page) and int(options.page, 10) if int(options.page, 10) > 0 else 1
    skip = (page - 1) * limit

    total_results = await collection.count_documents(filter).exec()
    results = await collection.find(filter).sort(sort_by).skip(skip).limit(limit)

    total_pages = ceil(total_results / limit)
    result = {
        'results': results,
        'page': page,
        'limit': limit,
        'totalPages': total_pages,
        'totalResults': total_results,
      }
    return result

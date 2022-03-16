from math import ceil

async def paginate(filter, options, collection):
    sort_by = ''
    if (options['sortBy']):
        sortingCriteria = []
        for sortOption in options['sortBy'].split(','):
            key, order = sortOption.split(':')
            sortingCriteria.append(('-' if order == 'desc' else '') + key)
        sort_by = ' '.join(sortingCriteria)
    else:
        sort_by = 'createdAt'

    limit = options.get('limit') and int(options['limit']) if int(options['limit']) > 0 else 10
    page = options.get('page') and int(options['page']) if int(options['page']) > 0 else 1
    skip = (page - 1) * limit
    filter = remove_none(filter)
    total_results = await collection.count_documents(filter)
    results = await collection.find(filter).sort(sort_by).skip(skip).limit(limit).to_list(length=limit)
    total_pages = ceil(total_results / limit)
    for result in results:
        result_clean_id(result)
    result = {
        'results': results,
        'page': page,
        'limit': limit,
        'totalPages': total_pages,
        'totalResults': total_results,
      }
    return result

def remove_none(dict_to_clean) -> dict:
    new_dict = {}
    for key, value in dict_to_clean.items():
        if value is None:
            continue
        elif isinstance(value, dict):
            new_dict[key] = remove_none(value)
        else:
            new_dict[key] = value
    return new_dict

def result_clean_id(dict_with_id) -> dict:
    del dict_with_id['_id']

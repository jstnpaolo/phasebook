from flask import Blueprint, request

from .data.search_data import USERS


bp = Blueprint("search", __name__, url_prefix="/search")


@bp.route("")
def search():
    return search_users(request.args.to_dict()), 200

def search_users(args):
    """Search users database

    Parameters:
        args: a dictionary containing the following search parameters:
            id: string
            name: string
            age: string
            occupation: string

    Returns:
        a list of users that match the search parameters
    """

    # Implement search here!
    id = args.get('id')
    name = args.get('name')
    age = args.get('age')
    occupation = args.get('occupation')

    if name:
        name = name.lower()
    if occupation:
        occupation = occupation.lower()
    if age:
        try:
            age = int(age)
        except ValueError:
            return []  # Invalid nteger return empty list

    result = []
    for user in USERS:
        
        if id is not None and str(user.get('id')) == id:
            result.append(user)
            continue
        if name is not None and name in user.get('name', '').lower():
            result.append(user)
            continue
        if age is not None and (age - 1 <= user.get('age', age) <= age + 1):
            result.append(user)
            continue
        if occupation is not None and occupation in user.get('occupation', '').lower():
            result.append(user)
            continue

    unique_result = {user['id']: user for user in result}.values() # remove duplicates

    
        # user['id'], user['name'], user['age'], user[occupation]))

    return list(unique_result)
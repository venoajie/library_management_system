from app.api import bp

@bp.route('/members/<int:id>', methods=['GET'])
def get_user(id):
    pass

@bp.route('/members', methods=['GET'])
def get_users():
    pass

@bp.route('/members/<int:id>/followers', methods=['GET'])
def get_followers(id):
    pass

@bp.route('/members/<int:id>/following', methods=['GET'])
def get_following(id):
    pass

@bp.route('/members', methods=['POST'])
def create_user():
    pass

@bp.route('/members/<int:id>', methods=['PUT'])
def update_user(id):
    pass
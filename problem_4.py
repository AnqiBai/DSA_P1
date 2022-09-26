class Group(object):
    def __init__(self, _name):
        self.name = _name
        self.groups = []
        self.users = []

    def add_group(self, group):
        self.groups.append(group)

    def add_user(self, user):
        self.users.append(user)

    def get_groups(self):
        return self.groups

    def get_users(self):
        return self.users

    def get_name(self):
        return self.name


parent = Group("parent")
child = Group("child")
sub_child = Group("subchild")

sub_child_user = "sub_child_user"
sub_child.add_user(sub_child_user)

child.add_group(sub_child)
parent.add_group(child)


def is_user_in_group(user, group):
    """
    Return True if user is in the group, False otherwise.

    Args:
      user(str): user name/id
      group(class:Group): group to check user membership against
    """
    if user is None or group is None or (not isinstance(user, str)) or (not isinstance(group, Group)):
        print('Invalid input')
        return False
    # check if the user is in current group
    if user in group.get_users():
        return True
    # check if the user is in children groups
    for subgroup in group.get_groups():
        if is_user_in_group(user, subgroup):
            return True

    return False


# Add your own test cases: include at least three test cases
# and two of them must include edge cases, such as null, empty or very large values

# Test Case 1
assert is_user_in_group(sub_child_user, parent) is True
# Test Case 2
assert is_user_in_group('incorrect_user', parent) is False
# Test Case 3 : test corner case
print(is_user_in_group(sub_child_user, 'parentGroup'))
# Test Case 4 : test a more complex case
parentGroup4 = Group("parent")
t_group = parentGroup4
for i in range(997):  # use 998 or higher number here will cause RecursionError
    depth = i
    child_group_name = 'child' + str(depth)
    child_group = Group(child_group_name)
    t_group.add_group(child_group)
    t_group = child_group
child_group.add_user('deep_user')
assert is_user_in_group('deep_user', parentGroup4) is True

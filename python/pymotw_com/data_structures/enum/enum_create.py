import enum

class BugStatus(enum.Enum):

    new = 7
    incomplete = 6
    invalid = 5
    wont_fix = 4
    in_poregress = 3
    fix_committed = 2
    fix_released = 1

print('\nMember name: {}'.format(BugStatus.wont_fix.name))
print('Member value: {}'.format(BugStatus.wont_fix.value))

print(vars(BugStatus))
print(BugStatus._member_map_)

for key, val in BugStatus._member_map_.items():
    print(key, '->' , val,  '->', val.value)

print('Enum Iteration starts'.center(100, '-'))
for status in BugStatus:
    print('{:15} = {}'.format(status.name, status.value))
print('Enum Iteration ends'.center(100, '-'))
print('Enum Comparation starts'.center(100, '-'))
actual_state = BugStatus.wont_fix
desired_state = BugStatus.fix_released

print("Equality:",
      actual_state == desired_state,
      actual_state == BugStatus.wont_fix)
print("Identity:",
      actual_state is desired_state,
      actual_state is BugStatus.wont_fix)
print('Enum Comparation ends'.center(100, '-'))




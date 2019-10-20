# The-elevator

#### The task is to process a string which represents levels in a building, where a given employee has access to.

This string contains comma-separated values:
Like: '1, -16, 3-4, -5-3, -8--11'
It can be a single [+/- number] or a range like [+/-number-(+/-number)]

#### Expected output:
A list of integers without duplicates where the employee can stop with the elevator.

#### Ex.
input  = '-16, 1, 1-7, -4-6, -1--4, 4--7' <br>
output = [-16, -7, -6, -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7]

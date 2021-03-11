items =[
    4,5,5,32,12,34,23,1,3
]

# Temporary sort
print('temporary sorted: ', sorted(items))

## Permament sort
items.sort()

print('sorted: ', items)

## Reverse sort
items.sort(reverse=True)

print('reverse: ', items)

## Finding length

print('The length of item is ' + str(len(items)))

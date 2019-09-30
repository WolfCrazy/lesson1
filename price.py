price = 100
discount = 5



def disc(price, discount, max_discount=50):
    price = abs(float(price))
    discount = abs(float(discount))
    max_discount=abs(float(max_discount))
    if max_discount>99:
        raise ValueError('Максимальная скидка не может быть больше 99%')
    if discount > max_discount:
        discount=max_discount
        return disc(price, discount)
    else:
        return price - (price*discount)/100

print(disc(price, discount))
print(disc(400, 500))
print(disc(-150, -15))

print(disc(150, 60))

print(disc(-150, 40, 100))
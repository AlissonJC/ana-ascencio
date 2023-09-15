price_factory, profit_seller_percent, tax_percent\
    = map(float, input().split())

profit_seller = price_factory * profit_seller_percent/100
taxes = price_factory * tax_percent/100

final_price = price_factory + profit_seller + taxes

print(f"{profit_seller:.2f}")
print(f"{taxes:.2f}")
print(f"{final_price:.2f}")
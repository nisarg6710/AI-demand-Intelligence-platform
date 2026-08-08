from src.inventory.service import InventoryService


service = InventoryService()


print("=" * 80)
print("INVENTORY SUMMARY")
print("=" * 80)

result = service.get_inventory_summary()

print(result)


print("\n" + "=" * 80)
print("FAST MOVING PRODUCTS")
print("=" * 80)

result = service.get_fast_moving_products()

print(result)


print("\n" + "=" * 80)
print("SLOW MOVING PRODUCTS")
print("=" * 80)

result = service.get_slow_moving_products()

print(result)


print("\n" + "=" * 80)
print("STORE DEMAND")
print("=" * 80)

result = service.get_store_inventory()

print(result)


print("\n" + "=" * 80)
print("REORDER CANDIDATES")
print("=" * 80)

result = service.get_reorder_candidates()

print(result)


print("\n" + "=" * 80)
print("INVENTORY HEALTH")
print("=" * 80)

result = service.get_inventory_health()

print(result)
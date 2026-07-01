import os
import json

ARCHIVE_DATE_BASE = "inventario_herbalife.json"

class Product:
    def __init__(self, name_product, price_full_canister, stock):
        self.name_product = name_product
        self.price_full_canister = price_full_canister
        self.stock = stock
    
    
    def to_dict(self):
        return self.__dict__
    
class Powdered_Product(Product):
    def __init__(self, name_product, price_full_canister, stock, price_for_unit, current_scoops, scoops_per_canister):
        super().__init__(name_product, price_full_canister, stock)
        self.price_for_unit = price_for_unit
        self.current_scoops = current_scoops
        self.scoops_per_canister = scoops_per_canister

    
    def to_dict(self):
        data = super().to_dict()
        data['price_for_unit'] = self.price_for_unit
        data['current_scoops'] = self.current_scoops
        data['scoops_per_canister'] = self.scoops_per_canister
        return data
    
class Sachet_Product(Product):
    def __init__(self, name_product, price_full_canister, stock, price_for_unit, current_sachets, sachet_per_canister):
        super().__init__(name_product, price_full_canister, stock)
        self.price_for_unit = price_for_unit
        self.current_sachets = current_sachets
        self.sachet_per_canister = sachet_per_canister

    
    def to_dict(self):
        data = super().to_dict()
        data['price_for_unit'] = self.price_for_unit 
        data['current_sachets'] = self.current_sachets
        data['sachet_per_canister'] = self.sachet_per_canister
        return data

class Tablet_Product(Product):
    def __init__(self, name_product, price_full_canister, stock, price_for_unit, current_capsule, capsule_per_canister):
        super().__init__(name_product, price_full_canister, stock)
        self.price_for_unit = price_for_unit
        self.current_capsule = current_capsule
        self.capsule_per_canister = capsule_per_canister

    
    def to_dict(self):
        data = super().to_dict()
        data['price_for_unit'] = self.price_for_unit
        data['current_capsule'] = self.current_capsule
        data['capsule_per_canister'] = self.capsule_per_canister
        return data

class Canister_Product(Product):
    def __init__(self, name_product, price_full_canister, stock):
        super().__init__(name_product, price_full_canister, stock)

def initial_database():
    initial_base = {

        "finance": {

            "daily_box": 0.0,
            "accumulated_losses": 0.0
        },

        "products": {

            "powdered_product": {

                #[][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][]
                # = = = = = = = = = =  LINEA DE PRODUCTOS (BATIDOS - 12 SABORES DIFERENTES)  = = = = = = = = = = =
                #[][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][]
                "Batido F1 Cookies": Powdered_Product("Batido F1 Cookies", 187.00, 12, 10.0, 42, 42),
                "Batido F1 Fresa": Powdered_Product("Batido F1 Fresa", 187.00, 4, 10.0, 42, 42),
                "Batido F1 Vainilla": Powdered_Product("Batido F1 Vainilla", 187.00, 3, 10.0, 42, 42),
                "Batido F1 Chocolate": Powdered_Product("Batido F1 Chocolate", 187.00, 3, 10.0, 42, 42),
                "Batido F1 Chocoavellana": Powdered_Product("Batido F1 Chocoavellana", 187.00, 3, 10.0, 42, 42),
                "Batido F1 Dulce de Leche": Powdered_Product("Batido F1 Dulce de Leche", 187.00, 3, 10.0, 42, 42),
                "Batido F1 Banana": Powdered_Product("Batido F1 Banana", 187.00, 1, 10.0, 42, 42),
                "Batido F1 Naranja": Powdered_Product("Batido F1 Naranja", 187.00, 3, 10.0, 42, 42),
                # - - - - - BATIDOS AÑADIDOS PARA COMPLETAR - - - - -
                "Batido F1 Piña Colada": Powdered_Product("Batido F1 Piña Colada", 187.00, 10, 10.0, 42, 42),
                "Batido F1 Café Latte": Powdered_Product("Batido F1 CAfé Latte", 187.00, 10, 10.0, 42, 42),
                "Batido F1 Frutos rojos": Powdered_Product("Batido F1 Frutos rojos", 187.00, 10, 10.0, 42, 42),
                "Batido F1 Maracuyá": Powdered_Product("Batido F1 Maracuyá", 187.00, 10, 10.0, 42, 42),


                #[][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][]
                # = = = = = = = = = = = =  LINEA DE PRODUCTOS (TÉS - 5 SABORES DIFERENTES)  = = = = = = = = = = = =
                #[][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][]
                "Té Durazno": Powdered_Product("Té Durazno", 147.00, 3, 4.0, 60, 60),
                "Té Frambuesa": Powdered_Product("Té Frambuesa", 147.00, 3, 4.0, 60, 60),
                # - - - - - - - - TÉS AÑADIDOS PARA COMPLETAR - - - - - - - -
                "Té Original": Powdered_Product("Té Original", 147.00, 10, 4.0, 60, 60),
                "Té Chal": Powdered_Product("Té Chal", 147.00, 10, 4.0, 60, 60),
                "Té Limón": Powdered_Product("Té Limón", 147.00, 10, 4.0, 60, 60),


                #[][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][]
                # = = = = = = = = = = =  OTROS TIPOS DE PRODUCTOS (9 PRODUCTOS)  = = = = = = = = = = = =
                #[][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][]
                "PDM": Powdered_Product("PDM", 238.00, 6, 6.0, 40, 40),
                "Drive": Powdered_Product("Drive", 146.00, 5, 5.0, 60, 60),
                "Polvo de Proteína": Powdered_Product("Polvo de Proteína", 152.00, 3, 6.0, 25, 25),
                "Beverage Mix": Powdered_Product("Beverage Mix", 162.00, 2, 6.0, 28, 28),
                "NRG Original": Powdered_Product("NRG Original", 113.00, 2, 5.0, 30, 30),
                "NRG Tropical": Powdered_Product("NRG Tropical", 113.00, 2, 5.0, 30, 30),
                "Bebida de colágeno": Powdered_Product("Bebida de colágeno", 207.00, 3, 7.0, 30, 30),
                "Fibra Manzana": Powdered_Product("Fibra Manzana", 210.00, 4, 6.0, 30, 30),
                "Beta Heart": Powdered_Product("Beta Heart", 239.00, 2, 8.0, 30, 30),

                #[][][][][][][][][] PRODUCTO LÍQUIDO AÑADIDO EXCEPCIÓN (1 PRODUCTO) [][][][][][][][][]
                "Aloe": Powdered_Product("Aloe", 183.00, 4, 6.0, 30, 30)
            },

            "sachet_product": {

                #[][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][]
                # = = = = = = = = = =  LINEA DE PRODUCTOS (2 PRODUCTOS)  = = = = = = = = = = = =
                #[][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][]
                "Liftoff": Sachet_Product("Liftoff", 84.00, 5, 8.0, 10, 10),
                "Golden Beverage": Sachet_Product("Golden Beverage", 159.00, 4, 10.0, 15, 15)
            },

            "tablet_product": {

                #[][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][]
                # = = = = = = = = = =  LINEA DE PRODUCTOS (3 PRODUCTOS)  = = = = = = = = = = = =
                #[][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][]
                "Omega": Tablet_Product("Omega", 183.00, 3, 3.5, 60, 60),
                "Multivitamínico": Tablet_Product("Multivitamínico", 83.00, 4, 1.0, 90, 90),
                "Calcio": Tablet_Product("Calcio", 77.00, 3, 1.0, 90, 90)
            },

            "canister_product": {

                #[][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][]
                # = = = = = = = = = =  LINEA DE PRODUCTOS (4 PRODUCTOS)  = = = = = = = = = = = =
                #[][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][]
                "Té Pomo": Canister_Product("Té Pomo", 147.00, 4),
                "Exfoliante": Canister_Product("Exfoliante", 101.00, 1),
                "Mascarilla": Canister_Product("Mascarilla", 109.00, 1),
                "Limpiador": Canister_Product("Limpiador", 129.00, 1)
            }
        }
    }

    save_datas(initial_base)


def validate_option(message, min_val=None, max_val=None):
    while True:
        try:
            choose_option = input(message).strip()

            if not choose_option:
                print('⚠️  [ERROR -- El campo no puede estar vacío. Reintente.]')
                continue

            whole = int(choose_option)

            if min_val is not None and whole < min_val:
                print(f'⚠️  [ERROR -- El valor no puede ser menor a {min_val}]')
                continue

            if max_val is not None and whole > max_val:
                print(f'⚠️  [ERROR -- El valor no puede ser mayor a {max_val}]')
                continue

            return whole
        
        except ValueError:
            print('⚠️  [ERROR -- Debe ingresar un número entero (No letras, ní símbolos)]')


def search_and_choose_product(inventory):
    all_products = []
    
    for category in inventory["products"].values():
        for name_product, obj in category.items():
            all_products.append({"name_product": name_product, "obj": obj})

    search_term = input('📋 Ingrese el nombre del producto a buscar: ').strip().lower()
    
    coincidences = [p for p in all_products if search_term in p["name_product"].lower()]

    if not coincidences:
        print('❌ [AVISO -- No se encontraron productos con ese término.]')
        return None
    
    print('\n' + '='*70)
    print(f"{'N°':<4} | {'PRODUCTO':<30} | {'PRECIO U.':<10} | {'STOCK TARROS':<10}")
    print('-'*70)

    for index, p in enumerate(coincidences, start=1):
        name_product = p["name_product"]
        obj = p["obj"]

        price_display = f"S/{obj.price_for_unit:.2f}" if hasattr(obj, 'price_for_unit') else "N/A"

        print(f"[{index:<2}] | {name_product:<30} | {price_display:<10} | {obj.stock:<10}")
    print('-'*70)

    selection = validate_option(f"👉 Seleccione el número (1-{len(coincidences)}): ", 1, len(coincidences))
    
    return coincidences[selection - 1]["obj"]


def load_datas():
    if not os.path.exists(ARCHIVE_DATE_BASE):
        initial_database()

    try:
        with open(ARCHIVE_DATE_BASE, "r", encoding="utf-8") as f:
            db = json.load(f)
    
    except json.JSONDecodeError:
        initial_database()
        with open(ARCHIVE_DATE_BASE, "r", encoding="utf-8") as f:
            db = json.load(f)

#[][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][]
# = = = = = = = =  ZONA DE RECONSTRUCCIÓN (Deserialización)  = = = = = = = = =0
#[][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][]
    for key, data in db["products"]["powdered_product"].items():
        db["products"]["powdered_product"][key] = Powdered_Product(
            data["name_product"], data["price_full_canister"], data["stock"],
            data["price_for_unit"], data["current_scoops"], data["scoops_per_canister"]
        )
    
    for key, data in db["products"]["sachet_product"].items():
        db["products"]["sachet_product"][key] = Sachet_Product(
            data["name_product"], data["price_full_canister"], data["stock"],
            data["price_for_unit"], data["current_sachets"], data["sachet_per_canister"]
        )
    
    for key, data in db["products"]["tablet_product"].items():
        db["products"]["tablet_product"][key] = Tablet_Product(
            data["name_product"], data["price_full_canister"], data["stock"],
            data["price_for_unit"], data["current_capsule"], data["capsule_per_canister"]
        )
    
    for key, data in db["products"]["canister_product"].items():
        db["products"]["canister_product"][key] = Canister_Product(
            data["name_product"], data["price_full_canister"], data["stock"]
        )
    
    return db


def save_datas(datas):
    with open(ARCHIVE_DATE_BASE, "w", encoding="utf-8") as f:
        json.dump(datas, f, indent=4, ensure_ascii=False, default=lambda o: o.to_dict())


def search_for_product_by_name(inventory, name):
    for category in inventory["products"].values():
        for prod in category.values():
            if prod.name_product == name:
                return prod
            
    return None
    

def register_sale(inventory):
    print('\n' + '='*70)
    print(' '*22, '🛒 REGISTRAR VENTAS 🛒')
    print('='*70)

    potion_rules = {
        "Aloe": 3,
        "Batido F1": 2, "Té": 2, "NRG": 2,
        "Beta Heart": 1, "Bebida de colágeno": 1, "Beverage Mix": 1, "PDM": 1, "Fibra": 1, "Drive": 1, "Golden Beverage": 1, "Liftoff": 1, "Omega": 1, "Multivitamínico": 1, "Calcio": 1,
        "default": 1
    }

    main_product = search_and_choose_product(inventory)

    if not main_product:
        return
    
    print("="*70)
    print(f"\n📦 Producto seleccionado: {main_product.name_product}")

    type_of_sale = validate_option("📠 ¿Que tipo de venta (1: Unidad / 2: Tarro Completo)?: ", 1, 2)

    total_amount_payable = 0.0
    final_order = []
    
    if type_of_sale == 1:
        qty = validate_option(f"🧮 ¿Cuánto {main_product.name_product} va a vender?: ", 1, 50)
        
        total_amount_payable += (main_product.price_for_unit * qty)
        
        for i in range(1, qty + 1):
            print(f"\n--- Configurando Producto N° {i} de {main_product.name_product} ---")

            if "Batido" in main_product.name_product:
                flavor = main_product.name_product.replace("Batido F1", "")

                if "Cookies" in flavor:
                    final_order.append({'name': "Batido F1 Cookies", 'qty': 2})
                else:
                    final_order.append({'name': "Batido F1 Cookies", 'qty': 1})
                    final_order.append({'name': main_product.name_product, 'qty': 1})
            else:
                qty_needed = next((v for k, v in potion_rules.items() if k in main_product.name_product), 1)
                final_order.append({'name': main_product.name_product, 'qty': qty_needed})
        
            if not isinstance(main_product, Tablet_Product):
                add_extra = validate_option(f"¿Agregar extra a la preparación N° {i}? (1. Sí / 2. No): ", 1, 2)

                if add_extra == 1:
                    extra = search_and_choose_product(inventory)
                    if extra:
                        final_order.append({'name': extra.name_product, 'qty': 1})
                        total_amount_payable += extra.price_for_unit      

    elif type_of_sale == 2:
        final_order.append({'name': main_product.name_product, 'qty': 1})
        total_amount_payable += main_product.price_full_canister

    for item in final_order:
        prod = search_for_product_by_name(inventory, item['name'])

        if type_of_sale == 2:
            prod.stock -= 1
        else:
            if isinstance(prod, Powdered_Product):
                attr = "current_scoops"
                max_cap = prod.scoops_per_canister
            elif isinstance(prod, Sachet_Product):
                attr = "current_sachets"
                max_cap = prod.sachet_per_canister
            elif isinstance(prod, Tablet_Product):
                attr = "current_capsule"
                max_cap = prod.capsule_per_canister
            else:
                continue 

            val = getattr(prod, attr) - item['qty']
            setattr(prod, attr, val)

            while getattr(prod, attr) < 0:
                prod.stock -= 1
                setattr(prod, attr, getattr(prod, attr) + max_cap)
    
    inventory["finance"]["daily_box"] += total_amount_payable
    save_datas(inventory)
    print(f"\n✅ Venta registrada. Total: S/{total_amount_payable:.2f}")


def add_stock(inventory):
    print('\n' + '='*70)
    print(' '*20, '📦 AGREGAR STOCK AL INVENTARIO 📦')
    print('='*70)

    term = search_and_choose_product(inventory)

    if not term:
        return
    
    print(f"\n✅ Producto seleccionado: {term.name_product}")
    print(f"🥫 Stock actual: {term.stock} tarros cerrados.")

    added_amount = validate_option("🔢 ¿Cuántos tarros desea agregar?: ", 1, 100)
    term.stock += added_amount

    save_datas(inventory)

    print(f"\n🎉 Stock actualizado")
    print('='*70)


def show_inventory(inventory):
    flavor_emojis = {
        "Batido F1 Cookies": "🍪", "Batido F1 Fresa": "🍓", "Batido F1 Vainilla": "🍦", "Batido F1 Chocolate": "🍫",
        "Batido F1 Chocoavellana": "🌰", "Batido F1 Dulce de Leche": "🍮", "Batido F1 Banana": "🍌", "Batido F1 Naranja": "🍊",
        "Batido F1 Piña Colada": "🍍", "Batido F1 Café Latte": "☕", "Batido F1 Frutos rojos": "🍒", "Batido F1 Maracuyá": "🥭",

        "Té Durazno": "🍑", "Té Frambuesa": "🍓", "Té Original": "🍵",
        "Té Chal": "🍓", "Té Limón": "🍋",

        "PDM": "🥛", "Drive": "⚡", "Polvo de Proteína": "💪", "Beverage Mix": "🍹",
        "NRG Original": "🔋", "NRG Tropical": "🌴", "Bebida de colágeno": "✨",
        "Fibra Manzana": "🍏", "Beta Heart": "🥛", "Aloe": "🌿",

        "Liftoff": "🧃", "Golden Beverage": "🧃",

        "Omega": "💊", "Multivitamínico": "💊", "Calcio": "💊",

        "Té Pomo": "🧴", "Exfoliante": "🧴", "Mascarilla": "🧴", "Limpiador": "🧴"
    }

    print('\n' + '='*120)
    print(' '*45, '📋 INVENTARIO TOTAL DEL NEGOCIO')
    print('='*120)
    print(f"{'SABOR DEL BATIDO':<29} | {'🥄 SCOOPS (USO/TOTAL)':<19} | {'💰 PRECIO VASO':<12} | {'🥫 STOCK TARROS':<14} | {'💵 PRECIO TARRO':<13} | {'📌 ESTADO':<10}")

    for name_product, obj in inventory["products"]["powdered_product"].items():
        servings_str = f"{obj.current_scoops}/{obj.scoops_per_canister}"
        price_str = f"S/{obj.price_for_unit:.2f}"
        stock_str = f"{obj.stock} cerrados"
        price_canister_str = f"S/{obj.price_full_canister:.2f}"

        state_flag = "❌ AGOTADO" if obj.stock == 0 else "🚨 CRÍTICO" if obj.stock == 1 else "✅ OK"
        emoji = flavor_emojis.get(name_product, "🥤")
        
        print(f"{emoji} {name_product:<26} | {servings_str:^21} | {price_str:<14} | {stock_str:<15} | {price_canister_str:<15} | {state_flag:<15}")
    
    for name_product, obj in inventory["products"]["sachet_product"].items():
        servings_str = f"{obj.current_sachets}/{obj.sachet_per_canister}"
        price_str = f"S/{obj.price_for_unit:.2f}"
        stock_str = f"{obj.stock} cerrados"
        price_canister_str = f"S/{obj.price_full_canister:.2f}"

        state_flag = "❌ AGOTADO" if obj.stock == 0 else "🚨 CRÍTICO" if obj.stock == 1 else "✅ OK"
        emoji = flavor_emojis.get(name_product, "🧃")

        print(f"{emoji} {name_product:<26} | {servings_str:^21} | {price_str:<14} | {stock_str:<15} | {price_canister_str:<15} | {state_flag:<15}")
    
    for name_product, obj in inventory["products"]["tablet_product"].items():
        servings_str = f"{obj.current_capsule}/{obj.capsule_per_canister}"
        price_str = f"S/{obj.price_for_unit:.2f}"
        stock_str = f"{obj.stock} cerrados"
        price_canister_str = f"S/{obj.price_full_canister:.2f}"

        state_flag = "❌ AGOTADO" if obj.stock == 0 else "🚨 CRÍTICO" if obj.stock == 1 else "✅ OK"
        emoji = flavor_emojis.get(name_product, "💊")
    
        print(f"{emoji} {name_product:<26} | {servings_str:^21} | {price_str:<14} | {stock_str:<15} | {price_canister_str:<15} | {state_flag:<10}")

    for name_product, obj in inventory["products"]["canister_product"].items():
        servings_str = "N/A"
        price_str = "N/A"
        stock_str = f"{obj.stock} cerrados"
        price_canister_str = f"S/{obj.price_full_canister:.2f}"

        state_flag = "❌ AGOTADO" if obj.stock == 0 else "🚨 CRÍTICO" if obj.stock == 1 else "✅ OK"
        emoji = flavor_emojis.get(name_product, "🧴") 
        
        print(f"{emoji} {name_product:<26} | {servings_str:^21} | {price_str:<14} | {stock_str:<15} | {price_canister_str:<15} | {state_flag:<10}") 
    
    print('='*120)


def show_daily_box(inventory):
    print('\n' + '='*70)
    print(' '*25, '💰 CAJA DIARIA 💰')
    print('='*70)
    
    total = inventory["finance"].get("daily_box", 0.0)
    
    print(f"\n💵 Total acumulado hoy: S/{total:.2f}")
    print('-'*70)
    
    print("¿Desea cerrar la caja del día y reiniciar a S/0.00?")
    option = validate_option("1: Sí, reiniciar caja / 2: No, mantener saldo: ", 1, 2)
    
    if option == 1:
        inventory["finance"]["daily_box"] = 0.0
        save_datas(inventory)
        print("\n✅ Caja reiniciada correctamente. ¡Listo para un nuevo día!")
    else:
        print("\n👍 El saldo actual se mantiene intacto.")
        
    print('='*70)


def interactive_menu():
    system_data = load_datas()

    while True:
        print('\n' + '='*13, 'SISTEMA DEL NEGOCIO HERBALIFE (SRA. NEDDA)', '='*13)
        print('[1] | Registrar una venta')
        print('[2] | Agregar stock al inventario')
        print('[3] | Mostrar el inventario')
        print('[4] | Ver y cerrar la caja diaria')
        print('[5] | Salir del sistema')

        option = validate_option('📋 Ingrese una opción del menú (1-5): ', min_val=1, max_val=4)

        if option == 1:
            register_sale(system_data)
        elif option == 2:
            add_stock(system_data)
        elif option == 3:
            show_inventory(system_data)
        elif option == 4:
            show_daily_box(system_data)
        elif option == 5:
            save_datas(system_data)
            print('\n' + '='*70)
            print(' '*1, '[👋 ¡Cierre de sistema, Sra. Nedda! Que tenga un excelente día.]')
            print('='*70)
            break
interactive_menu()
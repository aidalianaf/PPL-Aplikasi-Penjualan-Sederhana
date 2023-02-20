def addProduct(products, id_barang_new, nama_barang, harga_barang):
    # this function doesn't need return value
    products[id_barang_new] = {
            "id_barang": id_barang_new,
            "nama_barang": nama_barang,
            "harga_barang": harga_barang
        }
    # modify this pass with your own implementation

def calculateTotalPriceAfterDiscount(totalPrice):
    # this function need return value
    if totalPrice >= 150.000:
       totalPrice  = totalPrice * 90/100 
    elif totalPrice >= 500.000:
        totalPrice = totalPrice * 75/100
    return totalPrice 
    # modify this return with your own implementation (consider if else threshold for the discount)
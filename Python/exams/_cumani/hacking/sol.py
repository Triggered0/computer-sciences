# Load the products as a dictionary. The key are the product ids, and the corresponding values are the official reseller (string). There's no need for additional data structures since the official seller is unique.
def loadProducts(fname):

    hProductSellers = {}    
    f = open(fname)
    for line in f:
        fields = line.strip().split()
        product = fields[0]
        seller = fields[1]
        hProductSellers[product] = seller
    f.close()
        
    return hProductSellers

# Load the transactions in a dictionary. The keys are the product IDs. For each product, the corresponding value is the list of sellers taht sold that product
def loadTransactions(fname):

    hProductSellers = {}
    f = open(fname)
    for line in f:
        fields = line.strip().split()
        product = fields[0]
        seller = fields[1]

        if product not in hProductSellers:
            hProductSellers[product] = []
        hProductSellers[product].append(seller)
    f.close()

    return hProductSellers

# Print the suspect products. For each product (keys of hOfficialSellers) we create the list of unauthorized sellers, by selecting from the list of sellers those that are different from the official one.
# If the list of unautorized sellers is non-empty, we print the required information
def verifyTransactions(hOfficialSellers, hActualSellers):

    print("Suspect transactions")
    print()
    
    for product in sorted(hActualSellers): # sorting is not explicitly required by text
        unauthorizedSellers = set()
        for actualSeller in hActualSellers[product]:
            if actualSeller != hOfficialSellers[product]:
                unauthorizedSellers.add(actualSeller)
        if len(unauthorizedSellers) > 0:
            print("Product code:", product)
            print("Official seller:", hOfficialSellers[product])
            print("Sellers list: ", end = "")
            for seller in sorted(set(hActualSellers[product])): # We use a set to avoid printing the same seller more than once
                print(seller, end = " ")
            print()
            print()

def main():

    hOfficialSellers = loadProducts("products.txt")
    hTransactions = loadTransactions("transactions.txt")
    verifyTransactions(hOfficialSellers, hTransactions)

main()

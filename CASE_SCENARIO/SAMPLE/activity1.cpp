// Create a class called Invoice that a hardware store might use to represent an invoice for an item sold at the store. An Invoice should include four data members—a part number (type string), a part description (type string), a quantity of the item being purchased (type int) and a price per item (type int). Your class should have a constructor that initializes the four data members. A constructor that receives multiple arguments is defined with the form:
//         ClassName( TypeName1 parameterName1, TypeName2 parameterName2, ... )
// Provide a set and a get function for each data member. In addition, provide a member function named getInvoiceAmount that calculates the invoice amount (i.e., multiplies the quantity by the price per item), then returns the amount as an int value. If the quantity is not positive, it should be set to 0. If the price per item is not positive, it should be set to 0. Write a test program that demonstrates class Invoice’s capabilities.
#include<iostream>

class Invoice{

private: 
    std:: string partNumber;
    std:: string partDescription;
    int quantity;
    int pricePerItem;

public :

    Invoice(std::string partNumber, std:: string partDescription,int quantity , int pricePerItem){
    setPartNumber(partNumber);
    setPartDescription(partDescription);
    setQuantity(quantity);
    setPricePerItem(pricePerItem);
  
}
    void setPartNumber (std::string setPartNumber){
        this-> partNumber= partNumber;
    }
    std:: string getPartNumber(){
        return partNumber;
    }
    void setPartDescription (std::string PartDescription){
        this-> partDescription= partDescription;

    }
    std::string getPartDescription(){
        return partDescription;

    }
    void setQuantity (int quantity){
        if(quantity>0){
            this-> quantity= quantity ;
            }else{
                this->quantity=0;
            }
    }
    int getQuantity(){
        return quantity;
    }
    void setPricePerItem(int pricePerItem){
        if (pricePerItem>0){
            this-> pricePerItem=pricePerItem;

        }else{
            this-> pricePerItem=0;
        }
    }
        int getPricePerItem(){
            return pricePerItem;
        }
        int getInvoiceAmount (){
            return quantity * pricePerItem;

        }

    };


    int main(){
       Invoice  invoice1 ("1234", "Hammer", 2,10);
        Invoice invoice2 ("5678", "Screwdriver",-1,5);
        Invoice invoice3    ("9012","Pliers",3,-2);

        std :: cout <<"Invoice1 "<< std:: endl;
        std :: cout << "part Number: "<< invoice1.getPartNumber()<< std:: endl;
        std:: cout <<"part description"<< invoice1.getPartDescription()<<std:: endl;
        std ::cout<< "Quantity" << invoice1.getQuantity()<< std:: endl;
        std::cout << "Price per Item: " << invoice1.getPricePerItem() << std::endl;
    std::cout << "Invoice Amount: " << invoice1.getInvoiceAmount() << std::endl;

    std::cout << "\nInvoice 2:" << std::endl;
    std::cout << "Part Number: " << invoice2.getPartNumber() << std::endl;
    std::cout << "Part Description: " << invoice2.getPartDescription() << std::endl;
    std::cout << "Quantity: " << invoice2.getQuantity() << std::endl;
    std::cout << "Price per Item: " << invoice2.getPricePerItem() << std::endl;
    std::cout << "Invoice Amount: " << invoice2.getInvoiceAmount() << std::endl;

    std::cout << "\nInvoice 3:" << std::endl;
    std::cout << "Part Number: " << invoice3.getPartNumber() << std::endl;
    std::cout << "Part Description: " << invoice3.getPartDescription() << std::endl;
    std::cout << "Quantity: " << invoice3.getQuantity() << std::endl;
    std::cout << "Price per Item: " << invoice3.getPricePerItem() << std::endl;
    std::cout << "Invoice Amount: " << invoice3.getInvoiceAmount() << std::endl;

    return 0;
}
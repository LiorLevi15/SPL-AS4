from DTO import Hat
from DTO import Order
from DTO import Supplier
import sys
from repository import repo


def main():
    config = sys.argv[1];
    repo.create_tables();
    # handle config
    with open(config) as config:
        lines = config.readlines()
        num_of_stuff = lines[0].split(',');
        num_hats = int(num_of_stuff[0]);
        num_suppliers = int(num_of_stuff[1]);
        for x in range(1,1+num_hats):
            line = lines[x].split(',');
            id = int(line[0]);
            topping = line[1];
            supplier_for_hat = int(line[2]);
            quantity = int(line[3][:-1])
            repo.hats.insert(Hat(id, topping, supplier_for_hat, quantity))

        for x in range(1+num_hats, 1+num_hats+num_suppliers):
            line=lines[x].split(',');
            id = int(line[0]);
            name = line[1][:-1];
            if( x== num_hats+num_suppliers):
                name = line[1];
            repo.suppliers.insert(Supplier(id, name))

        #handle orders
        with open(sys.argv[2]) as argvs2:
            lines = argvs2.readlines()
            output = open(sys.argv[3], "w")
            for x in range(len(lines)):
                line=lines[x].split(',');
                location=line[0];
                topping=line[1][:-1];
                if x ==len(lines) -1:
                    topping = line[1];
                hat = repo.hats.order(topping)
                repo.orders.insert(Order(x + 1, location, hat[0]));
                supplier_boom = repo.suppliers.find(hat[1]);
                output.write(topping + "," + supplier_boom.name + "," + location + "\n")
        output.close()


if __name__ == "__main__":
    main()
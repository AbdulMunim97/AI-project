First of all, Install all the requirements to run this project by writing this command on the terminal. 
pip install -r requirements.txt 
This command will automaticaly install all the requirements to run this project.
After installing this run neo4j 
make a graph and put the details of the graph in coonection file in this line
graph = Graph("http://localhost:7474", auth=('neo4j', '123'))
After that just run the main file and you're good to go.
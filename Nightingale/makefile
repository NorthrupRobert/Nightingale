default: dataset.o dataset.h
	g++ -std=c++11 dataset.o dataset.h -o exe

dataset.o: dataset.cpp dataset.h
	g++ -std=c++11 -c dataset.cpp dataset.h

clean:
	rm *.o *.gch exe
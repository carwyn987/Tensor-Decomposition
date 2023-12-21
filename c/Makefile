CC=g++
CFLAGS=-Wall -I./include -I/home/carwyn/gsl/include
LDFLAGS = -L/home/carwyn/gsl/lib
LIBS = -lgsl -lgslcblas -lm
SRCDIR=./src
BUILDDIR=./build
DEPS = $(wildcard $(SRCDIR)/*.h)
SRC = $(wildcard $(SRCDIR)/*.cc)
OBJ = $(patsubst $(SRCDIR)/%.cc, $(BUILDDIR)/%.o, $(SRC))
TARGET = $(BUILDDIR)/out

$(BUILDDIR)/%.o: $(SRCDIR)/%.cc $(DEPS)
	$(CC) -c -o $@ $< $(CFLAGS)

$(TARGET): $(OBJ)
	$(CC) -o $@ $^ $(CFLAGS) $(LDFLAGS) $(LIBS)

.PHONY: all clean

all: $(TARGET)

clean:
	rm -f $(BUILDDIR)/*.o $(TARGET)
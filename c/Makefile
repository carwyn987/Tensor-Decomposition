CC=g++
CFLAGS=-I./include
SRCDIR=./src
BUILDDIR=./build
DEPS = $(wildcard $(SRCDIR)/*.h)
SRC = $(wildcard $(SRCDIR)/*.cc)
OBJ = $(patsubst $(SRCDIR)/%.cc, $(BUILDDIR)/%.o, $(SRC))
TARGET = $(BUILDDIR)/out

$(BUILDDIR)/%.o: $(SRCDIR)/%.cc $(DEPS)
	$(CC) -c -o $@ $< $(CFLAGS)

$(TARGET): $(OBJ)
	$(CC) -o $@ $^ $(CFLAGS)

.PHONY: all clean

all: $(TARGET)

clean:
	rm -f $(BUILDDIR)/*.o $(TARGET)

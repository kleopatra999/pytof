#include "UnionFind.h"
#include <vector>

class QuickUnionFind: public UnionFind
{
public:
    QuickUnionFind(int n);
    void print();
    bool find(int n, int p);
    void Union(int n, int p);

private:
    int root(int n);

    //
    // mVec is a forest (a list of tree)
    // Each entry contains its parent
    //
    std::vector<uint> mVec;
};


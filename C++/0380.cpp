#pragma GCC optimize("Ofast","inline","-ffast-math")
#pragma GCC target("avx,mmx,sse2,sse3,sse4")
class RandomizedSet {
public:
    RandomizedSet() {

    }
    
    bool insert(int val) {
        if (_um.find(val) != _um.end()) {
            return false;
        }

        _um[val] = _vals.size();
        _vals.push_back(val);

        return true;
    }
    
    bool remove(int val) {
        if (_um.find(val) == _um.end()) {
            return false;
        }

        int idx = _um[val];
        _um[_vals.back()] = idx;
        swap(_vals[idx], _vals.back());

        _um.erase(val);
        _vals.pop_back();

        return true;
    }
    
    int getRandom() {
        return _vals[rand() % _vals.size()];
    }

private:
    unordered_map<int, int> _um;
    vector<int> _vals;
};

/**
 * Your RandomizedSet object will be instantiated and called as such:
 * RandomizedSet* obj = new RandomizedSet();
 * bool param_1 = obj->insert(val);
 * bool param_2 = obj->remove(val);
 * int param_3 = obj->getRandom();
 */

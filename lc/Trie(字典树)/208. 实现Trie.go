
type Trie struct {
    m map[byte]*Trie
    end bool
}

func Constructor() Trie {
    return Trie{
        m: make(map[byte]*Trie),
        end: false,
    }
}


func (this *Trie) Insert(word string)  {
    node := this
    n := len(word)

    for i := 0; i < n; i++ {
        char := word[i]
        _, found := node.m[char]
        if !found {
            node.m[char] = &Trie{
                m: make(map[byte]*Trie),
                end: false,
            }
        }
        node = node.m[char]
    }
    node.end = true
}


func (this *Trie) Search(word string) bool {
    node := this
    n := len(word)
    for i := 0; i < n; i++ {
        char := word[i]
        _, found := node.m[char]
        if !found {
            return false
        }
        node = node.m[char]
    }
    if node.end != true {
        return false
    }

    return true
}


func (this *Trie) StartsWith(prefix string) bool {
    node := this
    n := len(prefix)
    for i := 0; i < n; i++ {
        char := prefix[i]
        _, found := node.m[char]
        if !found {
            return false
        }
        node = node.m[char]
    }

    return true
}


/**
 * Your Trie object will be instantiated and called as such:
 * obj := Constructor();
 * obj.Insert(word);
 * param_2 := obj.Search(word);
 * param_3 := obj.StartsWith(prefix);
 */
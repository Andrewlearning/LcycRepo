type Trie struct {
    m map[rune]*Trie
}


func Constructor() Trie {
    return Trie{
        m: make(map[rune]*Trie),
    }
}


func (this *Trie) Insert(word string)  {
    cm := this.m
    for _, char := range word {
        _, exist := cm[char]
        if !exist {
            cm[char] = &Trie{m: make(map[rune]*Trie)}
        }
        cm = cm[char].m
    }
    // 这里'#'是rune类型
    cm['#'] = nil
}


func (this *Trie) Search(word string) bool {
    cm := this.m
    for _, char := range word {
        _, exist := cm[char]
        if !exist {
            return false
        }
        cm = cm[char].m
    }
    // 这里'#'是rune类型
    _, exist := cm['#']
    if exist {
        return true
    }
    return false
}


func (this *Trie) StartsWith(prefix string) bool {
    cm := this.m
    for _, char := range prefix {
        _, exist := cm[char]
        if !exist {
            return false
        }
        cm = cm[char].m
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
package Hashmap


func isIsomorphic(s string, t string) bool {
	if len(s) != len(t) {
		return false
	}

	s2t := map[byte]byte{}
	t2s := map[byte]byte{}

	for i := range s {
		si := s[i]
		ti := t[i]
		if s2t[si] > 0 && s2t[si] != ti || t2s[ti] > 0 && t2s[ti] != si {
			return false
		}
		s2t[si] = ti
		t2s[ti] = si
	}

	return true

}

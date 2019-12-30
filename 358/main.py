#!/usr/bin/env python3

class ValueToKey(object):
    def __init__(self):
        self.bigger = -1
        self.smaller = -1
        self.keys = {}
    def add_key(self, key):
        self.keys[key] = True
    def remove_key(self, key):
        self.keys.pop(key)
    def get_key(self):
        return next(iter(self.keys))
    def is_empty(self):
        return len(self.keys) == 0


class DropThis(object):

    def __init__(self):
        self._keys_to_values = {}
        self._values_to_keys = {}
        self._max_value = 0
        self._min_value = 0

    def get_max(self):
        if not self._max_value:
            return None
        return self._values_to_keys[self._max_value].get_key()

    def get_min(self):
        if not self._min_value:
            return None
        return self._values_to_keys[self._min_value].get_key()

    def plus(self, k):
        if k not in self._keys_to_values:
            # New key
            self._keys_to_values[k] = 1
            if 1 not in self._values_to_keys:
                self._values_to_keys[1] = ValueToKey()
                self._values_to_keys[1].add_key(k)
                if not self._max_value:
                    self._max_value = 1
                if self._min_value:
                    # Updating the minimum
                    self._values_to_keys[self._min_value].smaller = 1
                    self._values_to_keys[1].bigger = self._min_value
                self._min_value = 1
            return
        old = self._keys_to_values[k]
        self._keys_to_values[k] = old + 1
        self._values_to_keys[old].remove_key(k)
        if self._values_to_keys[old].is_empty():
            self._values_to_keys[self._values_to_keys[old].before] = old + 1
            # This was the minimal value and now it increased
            if self._min_value == old:
                self._min_value += 1
            else:
                self._values_to_keys[self._values_to_keys[old].before] = old + 1
        if old + 1 not in self._values_to_keys:
            self._values_to_keys[old+1] = {k:True}
        else:
            self._values_to_keys[old+1][k] = True
        if self._max_value < old + 1:
            self._max_value = old + 1
        _ = self._values_to_keys.pop(old)

    def minus(self, k):
        if self._keys_to_values[k] == 1:
            _ = self._keys_to_values.pop(k)
            # remvoed the last element
            if not self._keys_to_values:
                self._values_to_keys = {}
                self._max_value = 0
                self._min_value = 0
                return
            self._values_to_keys[1].pop(k)
            # This is not the last element but it was the only one with value of 1
            if not self._values_to_keys[1]:
                pass
            return
        old = self._keys_to_values[k]
        self._keys_to_values[k] = old -1
        _ = self._values_to_keys[old].pop(k)
        if not self._values_to_keys[old]:
            _ = self._values_to_keys.pop(old)
            # This was the maximal value and now it decreased
            if self._max_value == old:
                self._max_value -= 1
        if old - 1 not in self._values_to_keys:
            self._values_to_keys[old-1] = {k:True}
        else:
            self._values_to_keys[old-1][k] = True
        if self._min_value > old - 1:
            self._min_value = old - 1


def main():
    pass


if __name__ == '__main__':
    main()


# Matt's solution modified
day_number = 5


def file_to_list():
    return_list = []
    data = open("./2023 Advent Calender/Day 5/data.txt")
    #data = open("./2023 Advent Calender/Day 5/test.txt")
    for line in data:
        clean_data = filter(None,line.lower().split("\n"))
        return_list += clean_data

    return return_list


input_data = file_to_list()


class DaySolution:
    def common(self, input_data):
        self.seeds = [int(i) for i in input_data[0].split(':')[1].split()]
        self.maps = []

        for line in input_data[1:]:
            if 'map' in line:
                self.maps.append([])
            elif line:
                dest, source, length = [int(i) for i in line.split()]
                # start, end, offset
                self.maps[-1].append((source,
                                      source + length - 1,
                                      dest - source))

    def part1(self, input_data):
        location = float('inf')

        for seed in self.seeds:
            p = seed

            for map_ in self.maps:
                for start, end, offset in map_:
                    if start <= p <= end:
                        p = p + offset
                        break

            location = min(location, p)

        return location

    def part2(self, input_data):
        ranges = []

        for i in range(0, len(self.seeds), 2):
            ranges.append((self.seeds[i],
                           self.seeds[i+1] + self.seeds[i] - 1))
            
        for map_ in self.maps:
            mapped_ranges = []

            for m_start, m_end, offset in map_:
                unmapped_ranges = []

                for r_start, r_end in ranges:
                    if m_end < r_start or r_end < m_start:
                        unmapped_ranges.append((r_start, r_end))
                    else:
                        left = max(m_start, r_start)
                        right = min(m_end, r_end)
                        mapped_ranges.append((left + offset, right + offset))

                        if r_start < left:
                            unmapped_ranges.append((r_start, left-1))

                        if right < r_end:
                            unmapped_ranges.append((right + 1, r_end))

                ranges = unmapped_ranges

            ranges = mapped_ranges + unmapped_ranges

        return min(l for (l, _) in ranges)
    


Day_5 = DaySolution()

Day_5.common(input_data)

print(f"Part 1: {Day_5.part1(input_data)}")
print(f"Part 2: {Day_5.part2(input_data)}")
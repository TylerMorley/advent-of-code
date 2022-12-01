#!/usr/bin/ruby

class Day01
  def get_elves (filename)
    elves = Array.new(0)
    elf = Array.new(0)

    File.readlines(filename).each do |line|
      line = line.strip
      if line != ""
        elf.append(line.to_i)
      else
        elves.append(elf)
        elf = Array.new(0)
      end
    end
    elves.append(elf)

    return elves
  end

  def get_calories (elves)
    elves_calories = Array.new(0)

    for i in 0..elves.length-1
      elf_calories = 0

      for j in 0..elves[i].length-1
        elf_calories += elves[i][j]
      end

      elves_calories.append(elf_calories)
    end
    
    return elves_calories.max
  end
end
    
day_one = Day01.new
input = day_one.get_elves('inputs/input01.txt')
output = day_one.get_calories(input)
print output.to_s + "\n"

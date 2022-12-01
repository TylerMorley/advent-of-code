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
    
    return elves_calories
  end

  def get_calories_top1 (calories_list)
    calories_list.max
  end

  def get_calories_top3 (calories_list)
    top_three = []
    for i in 0..2
      top_elf = calories_list.max
      top_three.append(top_elf)
      calories_list.delete(top_elf)
    end
    return top_three.sum
  end
end

if __FILE__ == $0    
  day_one = Day01.new
  input = day_one.get_elves('inputs/input01.txt')
  calories_list = day_one.get_calories(input)

  part1 = day_one.get_calories_top1(calories_list)
  print "Part 1:\n"
  print part1.to_s + "\n"
  part2 = day_one.get_calories_top3(calories_list)
  print "Part 2:\n"
  print part2.to_s + "\n"
end

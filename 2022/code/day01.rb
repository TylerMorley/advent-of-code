#!/usr/bin/ruby

class Day01
  def get_elves (filename)
    lines = File.read(filename).to_s
    elves_str = lines.split("\n\n").map{|elf| elf.split("\n")}
    elves = Array.new(0)

    for elf_str in elves_str
      elf = elf_str.map{|food_str| food_str.to_i}

      elves.append(elf)
    end

    return elves
  end

  def get_calories (elves)
    calory_totals = elves.map{|elf| elf.sum}
    return calory_totals
  end

  def get_calories_top1 (calories_list)
    return calories_list.max
  end

  def get_calories_top3 (calories_list)
    top_three = calories_list.sort[-3..]
    return top_three.sum
  end
end

if __FILE__ == $0    
  day_one = Day01.new
  input = day_one.get_elves('inputs/realinput01.txt')
  calories_list = day_one.get_calories(input)

  part1 = day_one.get_calories_top1(calories_list)
  print "Part 1:\n"
  print part1.to_s + "\n"
  part2 = day_one.get_calories_top3(calories_list)
  print "Part 2:\n"
  print part2.to_s + "\n"
end

#!/usr/bin/ruby
require 'set'

class Day03
  def get_rucksacks (filename)
    lines = File.read(filename).to_s
    rucksacks = lines.split("\n")

    return rucksacks
  end

  def compartmentalize (rucksacks)
    compartments = rucksacks.map do |sack|
      half = sack.length / 2
      first = sack.chars.take half
      second = sack.chars.drop half
      sack = [first.join, second.join]
    end
    return compartments
  end

  def find_error (rucksack)
    first = rucksack[0].chars.to_set
    second = rucksack[1].chars.to_set
    error = first.intersection(second).to_a[0]
  end

  def prioritize (error)
    priorities = ('a'..'z').to_a + ('A'..'Z').to_a
    priority = priorities.index(error) + 1
    return priority
  end

  def sum_priorities (rucksacks)
    sum = 0
    rucksacks.each do |sack|
      error = find_error(sack)
      priority = prioritize(error)
      sum += priority
    end
    return sum
  end
end

if __FILE__ == $0    
  day3 = Day03.new
  rucksacks = day3.get_rucksacks('inputs/realinput03.txt')
  compartmented = day3.compartmentalize(rucksacks)

  part1 = day3.sum_priorities(compartmented)
  print "Part 1:\n"
  print part1.to_s + "\n"
end

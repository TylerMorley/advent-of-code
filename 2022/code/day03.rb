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

  def group_rucksacks (rucksacks)
    groups = Array.new
    while rucksacks.length > 0 do
      group = rucksacks.shift 3
      groups.append(group)
    end
    return groups
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

  def get_badge (group)
    first = group[0].chars.to_set
    second = group[1].chars.to_set
    third = group[2].chars.to_set
    badge = first.intersection(second).intersection(third)
    return badge.to_a[0]
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

  def group_priorities (groups)
    sum = 0
    groups.each do |group|
      badge = get_badge(group)
      priority = prioritize(badge)
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

  groups = day3.group_rucksacks(rucksacks)
  part2 = day3.group_priorities(groups)
  print "Part 2:\n"
  print part2.to_s + "\n"
end

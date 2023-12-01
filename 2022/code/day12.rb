#!/usr/bin/ruby

class Day12
  def get_heightmap(filename)
    input = File.read(filename).split("\n").map{|row| row.chars}
  end

end

if __FILE__ == $0    
  day12 = Day12.new
  instructions = day12.get_input('inputs/realinput12.txt')
  monkeys = Array.new
  instructions.each do |instr|
    monkey = day12.make_monkey(instr, 1)
    monkeys.append(monkey)
  end

  part1 = day12.find_active_monkey(monkeys, 20)

  print "Part 1:\n"
  print part1.to_s + "\n"

  # instructions2 = day12.get_input('inputs/realinput12.txt')
  # monkeys2 = Array.new
  # instructions2.each do |instr|
  #   monkey = day12.make_monkey(instr, 2)
  #   monkeys.append(monkey)
  # end
  # part2 = day12.find_active_monkey(monkeys2, 10000)
  # print "Part 2:\n"
  # print part2.to_s + "\n"
end

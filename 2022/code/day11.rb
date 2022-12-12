#!/usr/bin/ruby

class Day11
  def get_input (filename)
    input = File.read(filename).split("\n\n").map{|monkey| monkey.split("\n").map{|line| line.strip}}
  end

  def make_monkey(input, part)
    id = input[0].delete('Monkey :').to_i
    items = input[1].delete('Starting items:').split(',').to_a.map{|x| x.to_i}
    operation = input[2][input[2].index('=') + 2..]
    test = input[3].delete('Test: divbly').to_i
    if_true = input[4].delete('If true: howomnky').to_i
    if_false= input[5].delete('If alse: throwomnky').to_i

    monkey = Monkey.new(id, items, operation, test, if_true, if_false, part)
  end

  def execute_round(monkies)
    monkies.each do |monkey|
      monkey.take_turn(monkies)
    end
  end

  def find_active_monkey(monkeys, rounds)
    activities = Array.new

    for i in 1..rounds
      execute_round(monkeys)
    end
    monkeys.each do |monkey|
      activities.append(monkey.num_inspected)
    end
    
    activities.sort!
    monkey_business = activities[-1] * activities[-2]
  end
end

class Monkey
  attr_accessor :id, :items, :operation, :test, :if_true, :if_false, :num_inspected, :part
  def initialize(id, items, operation, test, if_true, if_false, part)
    @id = id
    @items = items
    @operation = operation.split(' ')
    @test = test
    @if_true = if_true
    @if_false = if_false
    @num_inspected = 0
    @part = part
  end

  def inspect_item(item)
    first = item
    op = @operation[1]
    second = @operation[2] == 'old'? item : operation[2].to_i
    worry_level = 0

    if op == '+'
      worry_level = first + second
    elsif op == '*'
      worry_level = first * second
    end

    if @part == 1
      worry_level = (worry_level / 3).floor
    end
    return worry_level
  end

  def test_item(item)
    destination = nil
    if item % @test == 0
      destination = @if_true
    else
      destination = @if_false
    end
    return destination
  end

  def take_turn(monkeys)
    items_ = @items
    @items = Array.new
    items_.each do |item|
      worry_level = inspect_item(item)
      destination = test_item(worry_level)
      monkeys[destination].items.append(worry_level)
      @num_inspected += 1
    end
    return monkeys
  end
end

if __FILE__ == $0    
  day11 = Day11.new
  instructions = day11.get_input('inputs/realinput11.txt')
  monkeys = Array.new
  instructions.each do |instr|
    monkey = day11.make_monkey(instr, 1)
    monkeys.append(monkey)
  end

  part1 = day11.find_active_monkey(monkeys, 20)

  print "Part 1:\n"
  print part1.to_s + "\n"

  instructions2 = day11.get_input('inputs/realinput11.txt')
  monkeys2 = Array.new
  instructions2.each do |instr|
    monkey = day11.make_monkey(instr, 2)
    monkeys.append(monkey)
  end
  part2 = day11.find_active_monkey(monkeys2, 10000)
  print "Part 2:\n"
  print part2.to_s + "\n"
end

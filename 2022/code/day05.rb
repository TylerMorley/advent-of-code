#!/usr/bin/ruby

class Day05
  def get_input (filename)
    lines = File.read(filename).to_s.split("\n\n").map{|line| line = line.split("\n")}

    stacks = Array.new
    lines[0].pop
    lines[0].each do |row|
      stacks.append(refine_stacks(row))
    end
    
    procedures = Array.new
    lines[1].each do |row|
      procedures.append(refine_procedure(row))
    end

    input = [stacks, procedures]
    return input
  end

  def refine_crate(crate)
    output = nil
    crate.delete(' ')
    if crate.length > 0
      output = crate[1]
    end
    return output
  end

  def refine_stacks(row)
    refined = Array.new
    row_list = row.chars

    while row_list.length > 3 do
      entry = row_list.shift 4
      refined.append(refine_crate(entry))
    end
    refined.append(refine_crate(row_list))

    return refined
  end

  def refine_procedure(raw_procedure)
    procedure = Array.new
    words = ['move ', ' from ', ' to ']
    start_i = 0
    words.each do |word|
      if start_i > 0
        end_i = raw_procedure.index(word) - 1
        number = raw_procedure[start_i..end_i]
        procedure.append(number.to_i)
      end
      start_i = raw_procedure.index(word) + word.length
    end
    end_i = raw_procedure.index(words[-1]) + words[-1].length
    procedure.append(raw_procedure[end_i..].to_i)
    return procedure
  end

  def to_stacks(rows)
    stacks = rows.transpose
    output = Array.new
    stacks.each do |stack|
      stack.delete(nil)
      output.append(stack.reverse)
    end
    return output
  end

  def execute_step(stacks, step)
    quantity = step[0]
    origin = step[1]-1
    destination = step[2]-1

    for i in 1..quantity do
      temp = stacks[origin].pop()
      stacks[destination].push(temp)
    end
    return stacks
  end

  def execute_step_2(stacks, step)
    quantity = step[0]
    origin = step[1]-1
    destination = step[2]-1

    temp = stacks[origin].pop(quantity)
    stacks[destination] += temp
    return stacks
  end

  def execute_procedure(stacks, procedure, mode)
    procedure.each do |step|
      if mode == 1
        stacks = execute_step(stacks, step)
      elsif mode == 2
        stacks = execute_step_2(stacks, step)
      end
    end
    return stacks
  end

  def get_top_crates(stacks)
    output = ''
    stacks.each do |stack|
        output += stack.pop()
    end
    return output
  end
end

if __FILE__ == $0    
  day5 = Day05.new
  input = day5.get_input('inputs/realinput05.txt')
  stacks = day5.to_stacks(input[0])
  stacks2 = stacks.map{|x| x.dup}
  procedure = input[1]

  moved_stacks = day5.execute_procedure(stacks, procedure, 1)
  part1 = day5.get_top_crates(moved_stacks)
  print "Part 1:\n"
  print part1.to_s + "\n"

  moved_stacks2 = day5.execute_procedure(stacks2, procedure, 2)
  part2 = day5.get_top_crates(moved_stacks2)
  print "Part 2:\n"
  print part2.to_s + "\n"
end

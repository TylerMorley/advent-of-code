#!/usr/bin/ruby

class Day07
  def get_input (filename)
    File.read(filename).split("\n")
  end

  def organize(input)
    organized = Array.new
    
    command = nil
    location = nil
    results = Array.new
    input.each do |line|
      if line[0] == '$'
        if command == 'cd'
          organized.append([command, location])
        elsif command == 'ls'
          organized.append([command, results])
        end

        command = line[2..3]
        results = Array.new
        location = line[5..]
      else
        results.append(line)
      end
    end
    organized.append([command, results])

    return organized
  end

  def make_tree(instructions)
    root_instr = instructions[0]
    name = root_instr[1]
    root = FsNode.new(name)
    instructions.each do |instr|
      if instr[0] == 'ls'
        root.add_nodes(instr[1])
      end
    end
    return root
  end
end

class FsNode
  attr_accessor :name, :size, :parent, :children
  def initialize(name, size=nil, parent=nil, children=Array.new)
    @name = name
    @size = size
    @parent = parent
    @children = children
  end
end

if __FILE__ == $0    
  day7 = Day07.new
  input = day7.get_input('inputs/realinput07.txt')

  part1 = day6.get_sop_marker(input, distinct_chars)
  print "Part 1:\n"
  print part1.to_s + "\n"

  # part2 = day6.get_sop_marker(input, distinct_chars)
  # print "Part 2:\n"
  # print part2.to_s + "\n"
end

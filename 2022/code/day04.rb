#!/usr/bin/ruby
require 'set'

class Day04
  def get_assignments (filename)
    lines = File.read(filename).to_s
    assignments = lines.split("\n").map{
      |line| line.split(',').map{
        |pair| pair.split('-').map{
          |string| string.to_i
        }
      }
    }

    return assignments
  end

  def check_pair (pair)
    first = pair[0]
    second = pair[1]

    output = false
    if first[0] <= second[0] and first[1] >= second[1]
      output = true
    elsif second[0] <= first[0] and second[1] >= first[1]
      output = true
    end

    return output
  end

  def count_containments (assignments)
    count = 0
    assignments.each do |pair|
      if check_pair(pair)
        count += 1
      end
    end
    return count
  end
end

if __FILE__ == $0    
  day4 = Day04.new
  assignments = day4.get_assignments('inputs/realinput04.txt')

  part1 = day4.count_containments(assignments)
  print "Part 1:\n"
  print part1.to_s + "\n"
end

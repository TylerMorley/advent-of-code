#!/usr/bin/ruby
require 'set'

class Day06
  def get_input (filename)
    File.read(filename).to_s.strip
  end

  def get_sop_marker(buffer, distinct_chars)
    index = distinct_chars
    latest = buffer[..index-1].chars

    while latest.length != latest.to_set.length
      latest.shift
      latest.push(buffer[index])
      index += 1
    end
    return index
  end
end

if __FILE__ == $0    
  day6 = Day06.new
  input = day6.get_input('inputs/realinput06.txt')
  distinct_chars = 4

  part1 = day6.get_sop_marker(input, distinct_chars)
  print "Part 1:\n"
  print part1.to_s + "\n"

  distinct_chars = 14

  part2 = day6.get_sop_marker(input, distinct_chars)
  print "Part 2:\n"
  print part2.to_s + "\n"
end

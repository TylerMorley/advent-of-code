#!/usr/bin/ruby

class Day08
  def get_input (filename)
    File.read(filename).split("\n")
  end

end

if __FILE__ == $0    
  day8 = Day08.new
  input = day8.get_input('inputs/realinput07.txt')

  part1 = day8.get_sop_marker(input, distinct_chars)
  print "Part 1:\n"
  print part1.to_s + "\n"

  # part2 = day6.get_sop_marker(input, distinct_chars)
  # print "Part 2:\n"
  # print part2.to_s + "\n"
end

#!/usr/bin/ruby
require 'set'

class Day09
  def get_input (filename)
    input = File.read(filename).split("\n").map{|line| line.split(' ')}
    input.map{|line| [line[0], line[1].to_i]}
  end

  def move_head(head, direction)
    if direction == 'R'
      head[0] += 1
    elsif direction == 'L'
      head[0] -= 1
    elsif direction == 'U'
      head[1] += 1
    elsif direction == 'D'
      head[1] -= 1
    end
    return head
  end

  def move_tail(head, tail)
    horizontal = head[0] - tail[0]
    vertical = head[1] - tail[1]
    if horizontal.abs < 2 && vertical.abs < 2
      return tail
    elsif horizontal == 2 && vertical == 0
      tail[0] += 1
    elsif horizontal == 0 && vertical == 2
      tail[1] += 1
    elsif horizontal == -2 && vertical == 0
      tail[0] -= 1
    elsif horizontal == 0 && vertical == -2
      tail[1] -= 1
    elsif head[0] > tail[0] && head[1] > tail[1]
      tail[0] += 1
      tail[1] += 1
    elsif head[0] > tail[0] && head[1] < tail[1]
      tail[0] += 1
      tail[1] -= 1
    elsif head[0] < tail[0] && head[1] < tail[1]
      tail[0] -= 1
      tail[1] -= 1
    elsif head[0] < tail[0] && head[1] > tail[1]
      tail[0] -= 1
      tail[1] += 1
    end
    return tail
  end

  def move(knots, movement, visited)
    direction = movement[0]
    distance = movement[1]

    for i in 1..distance
      knots[0] = move_head(knots[0], direction)
      prev_knot = knots[0]
      for j in 1..knots.length-1
        knots[j] = move_tail(prev_knot, knots[j])
        prev_knot = knots[j]
      end
      visited = visit(visited, knots[-1])
    end

    return [knots, visited]
  end

  def visit(visited, tail)
    string_location = tail[0].to_s + 'x' + tail[1].to_s + 'y'
    visited.add(string_location)
  end

  def moves(knots, move_list)
    visited = Set.new

    move_list.each do |movement|
      output = move(knots, movement, visited)
      knots = output[0]
      visited = output[1]
    end

    return [knots, visited.length]
  end
end

if __FILE__ == $0    
  day9 = Day09.new
  input = day9.get_input('inputs/realinput09.txt')

  knots = [[0,0],[0,0]]
  part1 = day9.moves(knots, input)[1]
  print "Part 1:\n"
  print part1.to_s + "\n"

  knots2 = Array.new(10).map{|x| [0,0]}
  part2 = day9.moves(knots2, input)[1]
  print "Part 2:\n"
  print part2.to_s + "\n"
end

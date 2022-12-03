require 'test/unit'
require 'code/day03'

class Part1 < Test::Unit::TestCase
  def test_get_rucksacks
    day3 = Day03.new

    rucksacks = day3.get_rucksacks('inputs/testinput03.txt')
    expected = ['vJrwpWtwJgWrhcsFMMfFFhFp', 
                 'jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL', 
                 'PmmdzqPrVvPwwTWBwg', 
                 'wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn', 
                 'ttgJtRGJQctTZtZT', 
                 'CrZsJsPPZsGzwwsLwLmpwMDw'
               ]

    assert_equal expected, rucksacks
  end

  def test_compartmentalize
    day3 = Day03.new

    rucksacks = ['vJrwpWtwJgWrhcsFMMfFFhFp', 
                 'jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL', 
                 'PmmdzqPrVvPwwTWBwg', 
                 'wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn', 
                 'ttgJtRGJQctTZtZT', 
                 'CrZsJsPPZsGzwwsLwLmpwMDw'
               ]

    compartments = day3.compartmentalize(rucksacks)
    expected = [['vJrwpWtwJgWr','hcsFMMfFFhFp'], 
                 ['jqHRNqRjqzjGDLGL','rsFMfFZSrLrFZsSL'], 
                 ['PmmdzqPrV','vPwwTWBwg'], 
                 ['wMqvLMZHhHMvwLH','jbvcjnnSBnvTQFn'], 
                 ['ttgJtRGJ','QctTZtZT'], 
                 ['CrZsJsPPZsGz','wwsLwLmpwMDw']
               ]

    assert_equal expected, compartments
  end

  def test_find_error
    day3 = Day03.new
    rucksack = ['vJrwpWtwJgWr','hcsFMMfFFhFp']

    error = day3.find_error(rucksack)
    expected = 'p'

    assert_equal expected, error
  end    

  def test_prioritize
    day3 = Day03.new
    error = 'p'

    priority = day3.prioritize(error)
    expected = 16

    assert_equal expected, priority
  end

  def test_sum_priorities
    day3 = Day03.new
    rucksacks = [['vJrwpWtwJgWr','hcsFMMfFFhFp'], 
                 ['jqHRNqRjqzjGDLGL','rsFMfFZSrLrFZsSL'], 
                 ['PmmdzqPrV','vPwwTWBwg'], 
                 ['wMqvLMZHhHMvwLH','jbvcjnnSBnvTQFn'], 
                 ['ttgJtRGJ','QctTZtZT'], 
                 ['CrZsJsPPZsGz','wwsLwLmpwMDw']
               ]
    
    sum_priorities = day3.sum_priorities(rucksacks)
    expected = 157
    
    assert_equal expected, sum_priorities
  end
end

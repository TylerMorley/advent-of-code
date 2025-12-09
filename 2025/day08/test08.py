import unittest
import day08

class PartOne(unittest.TestCase):
    def setUp(self):
        self.circuits = [[[162, 817, 812]], [[57, 618, 57]], [[906, 360, 560]], [[592, 479, 940]],
                        [[352, 342, 300]], [[466, 668, 158]], [[542, 29, 236]], [[431, 825, 988]],
                        [[739, 650, 466]], [[52, 470, 668]], [[216, 146, 977]], [[819, 987, 18]],
                        [[117, 168, 530]], [[805, 96, 715]], [[346, 949, 466]], [[970, 615, 88]],
                        [[941, 993, 340]], [[862, 61, 35]], [[984, 92, 344]], [[425, 690, 689]]
                        ]
    def test_getInputs(self):
        junction_boxes = day08.getInputs('testinput08.txt')
        self.assertEqual(len(junction_boxes), 20)
        self.assertEqual(junction_boxes[0], [162,817,812])

    def test_measureDistance(self):
        j_box1 = [162,817,812]
        j_box2 = [425,690,689]
        distance = day08.measureDistance(j_box1, j_box2)
        self.assertEqual(distance, 316)

    def test_orderConnections(self):
        j_boxes = [[162, 817, 812], [57, 618, 57], [906, 360, 560], [592, 479, 940], [352, 342, 300], [466, 668, 158], [542, 29, 236], [431, 825, 988], [739, 650, 466], [52, 470, 668], [216, 146, 977], [819, 987, 18], [117, 168, 530], [805, 96, 715], [346, 949, 466], [970, 615, 88], [941, 993, 340], [862, 61, 35], [984, 92, 344], [425, 690, 689]]
        ordered = day08.orderConnections(j_boxes)
        distance, boxes = ordered[0]

        self.assertEqual(distance, 316)
        self.assertTrue([162,817,812] in boxes)
        self.assertTrue([425,690,689] in boxes)

        distance, boxes = ordered[1]
        self.assertEqual(distance, 321)
        self.assertTrue([162,817,812] in boxes)
        self.assertTrue([431,825,988] in boxes)

    def test_connect(self):
        circuits = self.circuits.copy()
        j_box1 = [162,817,812]
        j_box2 = [425,690,689]
        circuits = day08.connect(circuits, j_box1, j_box2)
        len_2_circuits = [x for x in circuits if len(x) == 2]
        self.assertEqual(len(len_2_circuits), 1)
        self.assertTrue([162,817,812] in len_2_circuits[0])
        self.assertTrue([425,690,689] in len_2_circuits[0])
        other_circuits = [x for x in circuits if len(x) == 1]
        self.assertEqual(len(other_circuits), 18)
        
        circuits = [[[162, 817, 812],[425,690,689]], [[57, 618, 57]], [[906, 360, 560]],
                    [[592, 479, 940]], [[352, 342, 300]], [[466, 668, 158]], [[542, 29, 236]],
                    [[431, 825, 988]], [[739, 650, 466]], [[52, 470, 668]], [[216, 146, 977]],
                    [[819, 987, 18]], [[117, 168, 530]], [[805, 96, 715]], [[346, 949, 466]],
                    [[970, 615, 88]], [[941, 993, 340]], [[862, 61, 35]], [[984, 92, 344]]
                    ]
        j_box1 = [162,817,812]
        j_box2 = [431,825,988]
        circuits = day08.connect(circuits, j_box1, j_box2)
        len_3_circuits = [x for x in circuits if len(x) == 3]
        self.assertEqual(len(len_3_circuits), 1)
        self.assertTrue([431,825,988] in len_3_circuits[0])

        circuits = self.circuits.copy()
        circuits.remove([[162,817,812]])
        circuits.remove([[425,690,689]])
        circuits.remove([[431,825,988]])
        circuits.append([[162,817,812],[425,690,689],[431,825,988]])
        j_box1 = [906,360,560]
        j_box2 = [805,96,715]
        circuits = day08.connect(circuits, j_box1, j_box2)
        len_2_circuits = [x for x in circuits if len(x) == 2]
        self.assertEqual(len(len_2_circuits), 1)
        self.assertTrue([906,360,560] in len_2_circuits[0])
        self.assertTrue([805,96,715] in len_2_circuits[0])
        
        circuits = self.circuits.copy()
        circuits.remove([[162,817,812]])
        circuits.remove([[425,690,689]])
        circuits.remove([[431,825,988]])
        circuits.append([[162,817,812],[425,690,689],[431,825,988]])
        circuits.remove([[906,360,560]])
        circuits.remove([[805,96,715]])
        circuits.append([[906,360,560],[805,96,715]])
        j_box1 = [431,825,988]
        j_box2 = [425,690,689]
        new_circuits = day08.connect(circuits, j_box1, j_box2)
        self.assertEqual(new_circuits, circuits)

    def test_getCircuitSizes(self):
        j_boxes = [[162, 817, 812], [57, 618, 57], [906, 360, 560], [592, 479, 940], [352, 342, 300], [466, 668, 158], [542, 29, 236], [431, 825, 988], [739, 650, 466], [52, 470, 668], [216, 146, 977], [819, 987, 18], [117, 168, 530], [805, 96, 715], [346, 949, 466], [970, 615, 88], [941, 993, 340], [862, 61, 35], [984, 92, 344], [425, 690, 689]]
        num_to_connect = 10
        circuit_sum = day08.getCircuitSizes(j_boxes, num_to_connect)
        self.assertEqual(circuit_sum, 40)

class PartTwo(unittest.TestCase):
    def test_makeLargeCircuit(self):
        j_boxes = [[162, 817, 812], [57, 618, 57], [906, 360, 560], [592, 479, 940], [352, 342, 300], [466, 668, 158], [542, 29, 236], [431, 825, 988], [739, 650, 466], [52, 470, 668], [216, 146, 977], [819, 987, 18], [117, 168, 530], [805, 96, 715], [346, 949, 466], [970, 615, 88], [941, 993, 340], [862, 61, 35], [984, 92, 344], [425, 690, 689]]
        cable_length_needed = day08.makeLargeCircuit(j_boxes)
        self.assertEqual(cable_length_needed, 25272)

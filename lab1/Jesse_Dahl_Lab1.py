#len_room = int(input("What is the length of the room (in feet)? "))
#wid_room = int(input("What is the width of the room (in feet)? "))
#len_table = int(input("What is the length of the table (in feet)? "))
#wid_table = int(input("What is the width of the table (in feet)? "))
space = int(input("How much space is required between tables (in feet)? "))
how_many = int(input("How many people does each table set? "))

space_req = (space * 4)

#room_area = (len_room * wid_room)
#table_area = (len_table * wid_table)

arrangement = (space_req * how_many)
print("This arrangement seats %s people" %(arrangement))



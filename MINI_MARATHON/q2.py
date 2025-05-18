# List of  dictionary given
cameras = [
    {'camera_type': 'Camera1', 'sensor_type': 'Radar', 'resolution': '1080p', 'field_of_view': 120},
    {'camera_type': 'Camera2', 'sensor_type': 'Lidar', 'resolution': '720p', 'field_of_view': 90},
    {'camera_type': 'Camera3', 'sensor_type': 'Radar', 'resolution': '720p', 'field_of_view': 90}
]

# Function to filter cameras by sensor type
def filter_by_sensor_type(sensor_type):
    try:
        return [camera for camera in cameras if camera['sensor_type'] == sensor_type]
    except KeyError as e:
        print(f"KeyError: {e}")
        return []

# Function to sort cameras by field_of_view in descending order
def sort_by_field_of_view():
    try:
        return sorted(cameras, key=lambda x: x['field_of_view'], reverse=True)
    except KeyError as e:
        print(f"KeyError: {e}")
        return []

# Function to update the resolution of all cameras
def update_resolution(new_resolution):
    try:
        for camera in cameras:
            camera['resolution'] = new_resolution
        return cameras
    except KeyError as e:
        print(f"KeyError: {e}")
        return []

# Function to calculate the total field_of_view of all cameras
def calculate_total_field_of_view():
    try:
        return sum(camera['field_of_view'] for camera in cameras)
    except KeyError as e:
        print(f"KeyError: {e}")
        return 0

# Function to search cameras within a field_of_view range
def search_in_range(min_view, max_view):
    try:
        return [camera for camera in cameras if min_view <= camera['field_of_view'] <= max_view]
    except KeyError as e:
        print(f"KeyError: {e}")
        return []

# Function to get keys with a given prefix
def get_keys_with_prefix(prefix):
    try:
        return [key for key in cameras[0].keys() if key.startswith(prefix)]
    except IndexError as e:
        print(f"IndexError: {e}")
        return []

# Function to get values with a given suffix
def get_values_with_suffix(suffix):
    try:
        values = []
        for camera in cameras:
            for value in camera.values():
                if isinstance(value, str) and value.endswith(suffix):
                    values.append(value)
        return values
    except Exception as e:
        print(f"Error: {e}")
        return []

# Function to calculate the average field_of_view of all cameras
def calculate_average_field_of_view():
    try:
        total_field_of_view = calculate_total_field_of_view()
        return total_field_of_view / len(cameras) if cameras else 0
    except ZeroDivisionError as e:
        print(f"ZeroDivisionError: {e}")
        return 0

# Test cases
print(filter_by_sensor_type("Radar"))  # Input: Radar
print(filter_by_sensor_type("Lidar"))  # Input: Lidar
print(sort_by_field_of_view())         # Sort by field_of_view
print(update_resolution("4K"))         # Update resolution to 4K
print(calculate_total_field_of_view()) # Calculate total field_of_view
print(search_in_range(90, 120))        # Input: 90, 120
print(search_in_range(130, 100))       # Input: 130, 100
print(get_keys_with_prefix("cam"))     # Input: cam
print(get_keys_with_prefix("res"))     # Input: res
print(get_values_with_suffix("p"))     # Input: suffix "p"
print(calculate_average_field_of_view()) # Calculate average field_of_view
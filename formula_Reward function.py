def reward_function(params):
    all_wheels_on_track = params['all_wheels_on_track']
    distance_from_center = params['distance_from_center']
    track_width = params['track_width']
    abs_steering = abs(params['steering_angle']) 
    closest_waypoints = params['closest_waypoints']

    if (closest_waypoints[0]>=0 and closest_waypoints[0]<=20) or (closest_waypoints[0]>=29 and closest_waypoints[0]<=47) or (closest_waypoints[0]>=92 and closest_waypoints[0]<=117) or (closest_waypoints[0]>167 and closest_waypoints[0]<200):
        params['speed']+=(4-params['speed'])*0.8
        marker_1 = 0.1 * track_width
        marker_2 = 0.25 * track_width
        marker_3 = 0.5 * track_width
        if distance_from_center <= marker_1:
            reward = 1.0
        elif distance_from_center <= marker_2:
            reward = 0.5
        elif distance_from_center <= marker_3:
            reward = 0.1
        else:
            reward = 1e-3

    else :
        marker_1 = 0.1 * track_width
        marker_2 = 0.25 * track_width
        marker_3 = 0.5 * track_width
        reward = 1e-3
        if all_wheels_on_track and (0.5*track_width - distance_from_center) >= 0.05:
            if distance_from_center <= marker_1:
                reward = 1.0
            elif distance_from_center <= marker_2:
                reward = 0.5
            elif distance_from_center <= marker_3:
                reward = 0.1
            else:
                reward = 1e-3
    
            ABS_STEERING_THRESHOLD = 15      
            if abs_steering > ABS_STEERING_THRESHOLD:
                reward *= 0.8   

    # return float(reward)
    print(reward)
    


if __name__ == "__main__":
    params={"all_wheels_on_track":True
    ,"distance_from_center":1.1
    ,"track_width":1.1
    ,"steering_angle":30
    ,"closest_waypoints":[1,2]
    ,"speed":1.4
    }
    print("start")
    reward_function(params)
    print("현재 속도",params['speed'])
    
   
//
//  Ketten.h
//  Ketten
//
//  Created by Oguzhan Yayla on 4/7/13.
//  Copyright (c) 2013 Oguzhan Yayla. All rights reserved.
//

#import <Foundation/Foundation.h>
#import <CoreData/CoreData.h>


@interface Ketten : NSManagedObject

@property (nonatomic, retain) NSNumber * id;
@property (nonatomic, retain) NSString * title;
@property (nonatomic, retain) NSDate * starting_date;
@property (nonatomic, retain) id links;

@end

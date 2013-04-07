//
//  AppDelegate.m
//  Ketten
//
//  Created by Oguzhan Yayla on 4/7/13.
//  Copyright (c) 2013 Oguzhan Yayla. All rights reserved.
//

#import "AppDelegate.h"
#import <Restkit/RestKit.h>
#import "Ketten.h"

@implementation AppDelegate

- (BOOL)application:(UIApplication *)application didFinishLaunchingWithOptions:(NSDictionary *)launchOptions
{
    // Override point for customization after application launch.
    
    RKObjectManager* objectManager = [RKObjectManager objectManagerWithBaseURLString:@"http://127.0.0.1:8000"];
    RKManagedObjectStore* objectStore = [RKManagedObjectStore objectStoreWithStoreFilename:@"Ketten.sqlite"];
    objectManager.objectStore = objectStore;
    objectManager.serializationMIMEType = RKMIMETypeJSON;
    
    RKManagedObjectMapping *kettenMapping = [RKManagedObjectMapping mappingForClass:[Ketten class] inManagedObjectStore:objectStore];
    
    [kettenMapping mapKeyPath:@"id" toAttribute:@"id"];
    [kettenMapping mapKeyPath:@"title" toAttribute:@"title"];
    [kettenMapping mapKeyPath:@"starting_date" toAttribute:@"starting_date"];
    [kettenMapping mapKeyPath:@"links" toAttribute:@"links"];
    
    kettenMapping.primaryKeyAttribute = @"id";
    [objectManager.mappingProvider addObjectMapping:kettenMapping];
    
    return YES;
}
							
- (void)applicationWillResignActive:(UIApplication *)application
{
    // Sent when the application is about to move from active to inactive state. This can occur for certain types of temporary interruptions (such as an incoming phone call or SMS message) or when the user quits the application and it begins the transition to the background state.
    // Use this method to pause ongoing tasks, disable timers, and throttle down OpenGL ES frame rates. Games should use this method to pause the game.
}

- (void)applicationDidEnterBackground:(UIApplication *)application
{
    // Use this method to release shared resources, save user data, invalidate timers, and store enough application state information to restore your application to its current state in case it is terminated later. 
    // If your application supports background execution, this method is called instead of applicationWillTerminate: when the user quits.
}

- (void)applicationWillEnterForeground:(UIApplication *)application
{
    // Called as part of the transition from the background to the inactive state; here you can undo many of the changes made on entering the background.
}

- (void)applicationDidBecomeActive:(UIApplication *)application
{
    // Restart any tasks that were paused (or not yet started) while the application was inactive. If the application was previously in the background, optionally refresh the user interface.
}

- (void)applicationWillTerminate:(UIApplication *)application
{
    // Called when the application is about to terminate. Save data if appropriate. See also applicationDidEnterBackground:.
}

@end

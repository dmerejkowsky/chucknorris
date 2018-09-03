@interface CKChuckNorris: NSObject

@property void* ckPtr;
+(NSString*) versionString;

-(instancetype)init;
-(NSString*) getFact;

@end

# General purpose
    # Amazon S3 Standard (S3 Standard)
        # S3 Standard offers high durability, availability, and performance object storage for frequently accessed data. 
        # Because it delivers low latency and high throughput, S3 Standard is appropriate for a wide variety of use cases, 
        # including cloud applications, dynamic websites, content distribution, mobile and gaming applications, and big 
        # data analytics. S3 Storage Classes can be configured at the object level and a single bucket can contain objects 
        # stored across S3 Standard, S3 Intelligent-Tiering, S3 Standard-IA, and S3 One Zone-IA. You can also use S3 
        # Lifecycle policies to automatically transition objects between storage classes without any application changes.
            # Key Features:
                # Low latency and high throughput performance
                # Designed for durability of 99.999999999% of objects across multiple Availability Zones
                # Resilient against events that impact an entire Availability Zone
                # Designed for 99.99% availability over a given year
                # Backed with the Amazon S3 Service Level Agreement for availability
                # Supports SSL for data in transit and encryption of data at rest
                # S3 Lifecycle management for automatic migration of objects to other S3 Storage Classes

# Infrequent access
    # Amazon S3 Standard-Infrequent Access (S3 Standard-IA)
        # S3 Standard-IA is for data that is accessed less frequently, but requires rapid access when needed. S3 Standard-IA 
        # offers the high durability, high throughput, and low latency of S3 Standard, with a low per GB storage price and 
        # per GB retrieval charge. This combination of low cost and high performance make S3 Standard-IA ideal for long-term 
        # storage, backups, and as a data store for disaster recovery files. S3 Storage Classes can be configured at the 
        # object level and a single bucket can contain objects stored across S3 Standard, S3 Intelligent-Tiering, S3 
        # Standard-IA, and S3 One Zone-IA. You can also use S3 Lifecycle policies to automatically transition objects between 
        # storage classes without any application changes.
            # Key Features:
            # Same low latency and high throughput performance of S3 Standard
            # Designed for durability of 99.999999999% of objects across multiple Availability Zones
            # Resilient against events that impact an entire Availability Zone
            # Data is resilient in the event of one entire Availability Zone destruction
            # Designed for 99.9% availability over a given year
            # Backed with the Amazon S3 Service Level Agreement for availability
            # Supports SSL for data in transit and encryption of data at rest
            # S3 Lifecycle management for automatic migration of objects to other S3 Storage Classes

    # Amazon S3 One Zone-Infrequent Access (S3 One Zone-IA)
        # S3 One Zone-IA is for data that is accessed less frequently, but requires rapid access when needed. Unlike other 
        # S3 Storage Classes which store data in a minimum of three Availability Zones (AZs), S3 One Zone-IA stores data 
        # in a single AZ and costs 20% less than S3 Standard-IA. S3 One Zone-IA is ideal for customers who want a lower-cost 
        # option for infrequently accessed data but do not require the availability and resilience of S3 Standard or S3 
        # Standard-IA. It’s a good choice for storing secondary backup copies of on-premises data or easily re-creatable 
        # data. You can also use it as cost-effective storage for data that is replicated from another AWS Region using 
        # S3 Cross-Region Replication.
            # Key Features:
            # Same low latency and high throughput performance of S3 Standard
            # Designed for durability of 99.999999999% of objects in a single Availability Zone†
            # Designed for 99.5% availability over a given year
            # Backed with the Amazon S3 Service Level Agreement for availability
            # Supports SSL for data in transit and encryption of data at rest
            # S3 Lifecycle management for automatic migration of objects to other S3 Storage Classes
# Archive
    # The Amazon S3 Glacier storage classes are purpose-built for data archiving. To move objects from Glacia back to
    # Standard tier, we have to restore them or copy them before we can move them.   
        # Amazon S3 Glacier Instant Retrieval
            # Amazon S3 Glacier Instant Retrieval is an archive storage class that delivers the lowest-cost storage for 
            # long-lived data that is rarely accessed and requires retrieval in milliseconds. With S3 Glacier Instant 
            # Retrieval, you can save up to 68% on storage costs compared to using the S3 Standard-Infrequent Access 
            # (S3 Standard-IA) storage class, when your data is accessed once per quarter. S3 Glacier Instant Retrieval 
            # delivers the fastest access to archive storage, with the same throughput and milliseconds access as the 
            # S3 Standard and S3 Standard-IA storage classes. S3 Glacier Instant Retrieval is ideal for archive data that 
            # needs immediate access, such as medical images, news media assets, or user-generated content archives. 
            # You can upload objects directly to S3 Glacier Instant Retrieval, or use S3 Lifecycle policies to transfer 
            # data from the S3 storage classes.
                # Key Features:
                    # Data retrieval in milliseconds with the same performance as S3 Standard
                    # Designed for durability of 99.999999999% of objects across multiple Availability Zones
                    # Data is resilient in the event of the destruction of one entire Availability Zone
                    # Designed for 99.9% data availability in a given year
                    # 128 KB minimum object size
                    # Backed with the Amazon S3 Service Level Agreement for availability
                    # S3 PUT API for direct uploads to S3 Glacier Instant Retrieval, and S3 Lifecycle management 
                    # for automatic migration of objects
                    # 90 days minimum storage duration

        # Amazon S3 Glacier Flexible Retrieval (Formerly S3 Glacier)
            # S3 Glacier Flexible Retrieval delivers low-cost storage, up to 10% lower cost (than S3 Glacier Instant 
            # Retrieval), for archive data that is accessed 1—2 times per year and is retrieved asynchronously. For 
            # archive data that does not require immediate access but needs the flexibility to retrieve large sets of 
            # data at no cost, such as backup or disaster recovery use cases, S3 Glacier Flexible Retrieval (formerly 
            # S3 Glacier) is the ideal storage class. S3 Glacier Flexible Retrieval delivers the most flexible 
            # retrieval options that balance cost with access times ranging from minutes to hours and with free bulk 
            # retrievals. It is an ideal solution for backup, disaster recovery, offsite data storage needs, and for 
            # when some data occasionally need to be retrieved in minutes, and you don’t want to worry about costs. 
            # S3 Glacier Flexible Retrieval is designed for 99.999999999% (11 9s) of data durability and 99.99% 
            # availability by redundantly storing data across multiple physically separated AWS Availability Zones in a 
            # given year.
                # Key Features:
                    # Designed for durability of 99.999999999% of objects across multiple Availability Zones
                    # Data is resilient in the event of one entire Availability Zone destruction
                    # Supports SSL for data in transit and encryption of data at rest
                    # Ideal for backup and disaster recovery use cases when large sets of data occasionally need 
                    # to be retrieved in minutes, without concern for costs
                    # Configurable retrieval times, from minutes to hours, with free bulk retrievals
                    # S3 PUT API for direct uploads to S3 Glacier Flexible Retrieval, and S3 Lifecycle management 
                    # for automatic migration of objects
                    # 90 days minimum storage duration
                    # Expedited (1-5 mins), Standard (3-5 hours) and Bulk (5-12 hours)

        # Amazon S3 Glacier Deep Archive
            # S3 Glacier Deep Archive is Amazon S3’s lowest-cost storage class and supports long-term retention and 
            # digital preservation for data that may be accessed once or twice in a year. It is designed for 
            # customers—particularly those in highly-regulated industries, such as financial services, healthcare, and 
            # public sectors—that retain data sets for 7—10 years or longer to meet regulatory compliance requirements. 
            # S3 Glacier Deep Archive can also be used for backup and disaster recovery use cases, and is a cost-effective 
            # and easy-to-manage alternative to magnetic tape systems, whether they are on-premises libraries or 
            # off-premises services. S3 Glacier Deep Archive complements Amazon S3 Glacier, which is ideal for archives 
            # where data is regularly retrieved and some of the data may be needed in minutes. All objects stored in S3 
            # Glacier Deep Archive are replicated and stored across at least three geographically-dispersed Availability 
            # Zones, protected by 99.999999999% of durability, and can be restored within 12 hours.
                # Key Features:
                    # Designed for durability of 99.999999999% of objects across multiple Availability Zones
                    # Lowest cost storage class designed for long-term retention of data that will be retained for 7-10 
                    # years
                    # Ideal alternative to magnetic tape libraries
                    # Retrieval time within 12 hours
                    # S3 PUT API for direct uploads to S3 Glacier Deep Archive, and S3 Lifecycle management for automatic 
                    # migration of objects
                    # 180 days minimum storage duration
                    # Standard (12 hours) and Bulk (48 hours)
 
# Unknown or changing access
    # Amazon S3 Intelligent-Tiering (S3 Intelligent-Tiering)
        # Amazon S3 Intelligent-Tiering (S3 Intelligent-Tiering) is the first cloud storage that automatically reduces 
        # your storage costs on a granular object level by automatically moving data to the most cost-effective access 
        # tier based on access frequency, without performance impact, retrieval fees, or operational overhead. S3 
        # Intelligent-Tiering delivers milliseconds latency and high throughput performance for frequently, infrequently, 
        # and rarely accessed data in the Frequent, Infrequent, and Archive Instant Access tiers. You can use S3 
        # Intelligent-Tiering as the default storage class for virtually any workload, especially data lakes, data analytics, 
        # new applications, and user-generated content.
        # For a small monthly object monitoring and automation charge, S3 Intelligent-Tiering monitors access patterns 
        # and automatically moves objects that have not been accessed to lower-cost access tiers. S3 Intelligent-Tiering 
        # automatically stores objects in three access tiers: one tier that is optimized for frequent access, a 40% 
        # lower-cost tier that is optimized for infrequent access, and a 68% lower-cost tier optimized for rarely accessed 
        # data. S3 Intelligent-Tiering monitors access patterns and moves objects that have not been accessed for 30 
        # consecutive days to the Infrequent Access tier and after 90 days of no access to the Archive Instant Access 
        # tier. For data that does not require immediate retrieval, you can set up S3 Intelligent-Tiering to monitor 
        # and automatically move objects that aren’t accessed for 180 days or more to the Deep Archive Access tier to 
        # realize up to 95% in storage cost savings. There are no retrieval charges in S3 Intelligent-Tiering. If an object 
        # in the Infrequent or Archive Instant Access tier is accessed later, it’s automatically moved back to the Frequent 
        # Access tier. If the object you’re retrieving is stored in the optional Deep Archive tiers, before you can retrieve 
        # the object, you must first restore a copy using RestoreObject. 
            # Key Features:
                # Frequent, Infrequent, and Archive Instant Access tiers have the same low-latency and high-throughput 
                # performance of S3 Standard 
                # The Infrequent Access tier saves up to 40% on storage costs
                # The Archive Instant Access tier saves up to 68% on storage costs 
                # Opt-in asynchronous archive capabilities for objects that become rarely accessed 
                # Deep Archive Access tier has the same performance as Glacier Deep Archive and saves up to 95% for rarely 
                # accessed objects
                # Designed for durability of 99.999999999% of objects across multiple Availability Zones and for 99.9% 
                # availability over a given year
                # Backed with the Amazon S3 Service Level Agreement for availability
                # Small monthly monitoring and auto tiering charge
                # No operational overhead, no lifecycle charges, no retrieval charges, and no minimum storage duration
                # Objects smaller than 128KB can be stored in S3 Intelligent-Tiering but will always be charged at the 
                # Frequent Access tier rates, and are not charged the monitoring and automation charge. 
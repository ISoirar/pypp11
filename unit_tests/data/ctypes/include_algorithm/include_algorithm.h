#pragma once

#include "libconfig.h"

struct EXPORT_SYMBOL io_marker_t{};

struct EXPORT_SYMBOL io_file_t{
    io_marker_t* io_marker;
};

void EXPORT_SYMBOL do_nothing( io_file_t* );
